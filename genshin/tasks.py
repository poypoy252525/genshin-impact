from django.core.files.base import ContentFile
import requests
from genshin_scraper import GenshinScraper
from celery import shared_task
from .models import Artifact, Rarity

@shared_task
def scrape_artifacts(force_update=False):
    scraper = GenshinScraper()
    artifacts = scraper.get_artifact_list()
    
    artifacts_data = artifacts['data']['items']
    
    for artifact_info in artifacts_data.values():
        response = requests.get(f'{scraper.base_url}/reliquary/{artifact_info["id"]}')
        artifact_detail = response.json()['data']
        
        artifact_obj, created = Artifact.objects.update_or_create(
            source_id=artifact_detail['id'],
            defaults={
                'name': artifact_detail['name'],
            }
        )
        
        # Download and save the actual image if it doesn't have one, if it was just created,
        # or if it only contains the legacy raw string (not a file path)
        icon_name = artifact_detail['icon']
        is_legacy_string = artifact_obj.icon and not str(artifact_obj.icon.name).startswith('images/artifacts/')
        
        if force_update or created or not artifact_obj.icon or is_legacy_string:
            if icon_name:
                image_url = f"https://gi.yatta.moe/assets/UI/reliquary/{icon_name}.png"
                try:
                    img_response = requests.get(image_url, timeout=30)
                    img_response.raise_for_status()
                    
                    # Wrap the content in a ContentFile and save to the ImageField
                    artifact_obj.icon.save(
                        f"{icon_name}.png",
                        ContentFile(img_response.content),
                        save=True
                    )
                    print(f"Successfully downloaded image for: {artifact_obj.name}")
                except Exception as e:
                    print(f"Failed to download image for artifact {artifact_detail['name']}: {e}")
        
        for rarity_val in artifact_detail['levelList']:
            rarity_obj, _ = Rarity.objects.get_or_create(
                level=f'{rarity_val}',
            )
            artifact_obj.rarities.add(rarity_obj)
        

    return artifacts_data