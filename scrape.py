import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

import argparse
import logging
import time
from genshin.tasks import scrape_artifacts, scrape_materials

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger("scrape_script")

parser = argparse.ArgumentParser(description="Scrape Genshin artifacts and images.")
parser.add_argument("--force", "-f", action="store_true", help="Force update of all images")
parser.add_argument("--async", "-a", dest="is_async", action="store_true", help="Run as a background Celery task")
args = parser.parse_args()

start_time = time.time()
logger.info("Script started.")

try:
    if args.is_async:
        logger.info("Triggering scrape_artifacts task in background...")
        # Since scrape_artifacts is decorated with @shared_task, we use .delay()
        scrape_artifacts.delay(force_update=args.force)
        scrape_materials.delay(force_update=args.force)
        logger.info("Task triggered. Check Celery logs or worker output for progress.")
    else:
        result = scrape_artifacts(force_update=args.force)
        result = scrape_materials(force_update=args.force)
        elapsed_time = time.time() - start_time
        logger.info(f"Script finished successfully in {elapsed_time:.2f} seconds.")
except KeyboardInterrupt:
    logger.warning("Script interrupted by user.")
except Exception as e:
    logger.error(f"Script failed with error: {e}")
