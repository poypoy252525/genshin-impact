import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from genshin.tasks import scrape_artifacts

result = scrape_artifacts()
