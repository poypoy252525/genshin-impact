import requests
from genshin_scraper import GenshinScraper
from celery import shared_task
from .models import Artifact, Rarity

@shared_task
def scrape_artifacts():
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
                'icon': artifact_detail['icon'],
            }
        )
        
        for rarity_val in artifact_detail['levelList']:
            rarity_obj, _ = Rarity.objects.get_or_create(
                level=f'{rarity_val}',
            )
            artifact_obj.rarities.add(rarity_obj)
        

    return artifacts_data