from genshin_scraper import GenshinScraper
from celery import shared_task

@shared_task
def get_character_list():
    scraper = GenshinScraper()
    characters = scraper.get_character_list()
    # Removed debug print to avoid encoding issues on some consoles

    return characters