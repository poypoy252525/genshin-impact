from genshin.models import ArtifactSuitType
from genshin.models import ArtifactSuit
from genshin.models import ArtifactAffixList
from django.core.files.base import ContentFile
import requests
from genshin_scraper import GenshinScraper
from celery import shared_task
from .models import Artifact, Rarity
import logging

logger = logging.getLogger(__name__)

@shared_task
def scrape_artifacts(force_update=False):
    logger.info("Starting Genshin artifacts scraping process...")
    scraper = GenshinScraper()
    
    try:
        artifacts = scraper.get_artifact_list()
        artifacts_data = artifacts['data']['items']
        total_artifacts = len(artifacts_data)
        logger.info(f"Retrieved {total_artifacts} artifacts from scraper.")
    except Exception as e:
        logger.error(f"Failed to retrieve artifact list: {e}")
        return {}

    processed_count = 0
    success_count = 0
    error_count = 0

    for source_id, artifact_info in artifacts_data.items():
        processed_count += 1
        artifact_name = artifact_info.get('name', 'Unknown')
        logger.info(f"[{processed_count}/{total_artifacts}] Processing artifact: {artifact_name} (ID: {source_id})")
        
        try:
            response = requests.get(f'{scraper.base_url}/reliquary/{source_id}')
            response.raise_for_status()
            artifact_detail = response.json()['data']
            
            artifact_obj, created = Artifact.objects.update_or_create(
                source_id=artifact_detail['id'],
                defaults={
                    'name': artifact_detail['name'],
                }
            )
            
            if created:
                logger.info(f"Created new artifact record for: {artifact_name}")
            else:
                logger.debug(f"Updated existing artifact record for: {artifact_name}")
            
            # Download and save the actual image
            icon_name = artifact_detail.get('icon')
            is_legacy_string = artifact_obj.icon and not str(artifact_obj.icon.name).startswith('images/artifacts/')
            
            if force_update or created or not artifact_obj.icon or is_legacy_string:
                if icon_name:
                    image_url = f"https://gi.yatta.moe/assets/UI/reliquary/{icon_name}.png"
                    try:
                        logger.info(f"Downloading image for {artifact_name}: {image_url}")
                        img_response = requests.get(image_url, timeout=30)
                        img_response.raise_for_status()
                        
                        artifact_obj.icon.save(
                            f"{icon_name}.png",
                            ContentFile(img_response.content),
                            save=True
                        )
                        logger.info(f"Successfully saved image for: {artifact_name}")
                    except Exception as e:
                        logger.warning(f"Failed to download image for {artifact_name}: {e}")
            
            # Handle rarities
            for rarity_val in artifact_detail.get('levelList', []):
                rarity_obj, _ = Rarity.objects.get_or_create(
                    level=f'{rarity_val}',
                )
                artifact_obj.rarities.add(rarity_obj)
            
            # Handle affix list
            for affix_name in artifact_detail.get('affixList', {}).values():
                affix_obj, _ = ArtifactAffixList.objects.update_or_create(
                    name=affix_name,
                    defaults={
                        'name': affix_name,
                    }
                )
                artifact_obj.affix_list.add(affix_obj)
            
            # Handle suit pieces
            for piece_type, piece_data in artifact_detail.get('suit', {}).items():
                suit_obj, _ = ArtifactSuit.objects.update_or_create(
                    name=piece_data['name'],
                    defaults={
                        'description': piece_data.get('description'),
                        'type': piece_type,
                        'max_level': piece_data.get('maxLevel'),
                    }
                )
                artifact_obj.suit.add(suit_obj)
                
            
            success_count += 1
        except Exception as e:
            error_count += 1
            logger.error(f"Error processing artifact {artifact_name} ({source_id}): {e}")
        
    logger.info(f"Scraping completed. Total: {total_artifacts}, Success: {success_count}, Errors: {error_count}")
    return artifacts_data
