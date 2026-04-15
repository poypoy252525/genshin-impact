import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

import argparse
from genshin.tasks import scrape_artifacts

parser = argparse.ArgumentParser(description="Scrape Genshin artifacts and images.")
parser.add_argument("--force", "-f", action="store_true", help="Force update of all images")
args = parser.parse_args()

result = scrape_artifacts(force_update=args.force)
