from celery import shared_task

@shared_task
def run_scraper():
    print("Running scraper...")