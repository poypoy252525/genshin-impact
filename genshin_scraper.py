import requests
from bs4 import BeautifulSoup

class GenshinScraper:
    
    def __init__(self, base_url: str = 'https://genshin-impact.fandom.com'):
        self.base_url = base_url
        self.api_url = f"{base_url}/api.php"
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

    def get_character_list(self):
        # The MediaWiki API is designed for bots and won't 403 like the main site URL.
        # action=parse lets us get the HTML of the Character/List page directly.
        params = {
            "action": "parse",
            "page": "Character/List",
            "format": "json",
            "prop": "text",
            "redirects": 1
        }
        
        headers = {
            "User-Agent": self.user_agent
        }

        try:
            response = requests.get(self.api_url, params=params, headers=headers, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            if 'error' in data:
                print(f"API Error: {data['error'].get('info')}")
                return []
            
            # Removed debug print to avoid encoding issues on some consoles

                
            html_content = data['parse']['text']['*']
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Find all relevant tables
            tables = soup.select('table.fandom-table')
            characters = []

            for table in tables:
                rows = table.find_all('tr')[1:] # Skip header
                for row in rows:
                    cols = row.find_all('td')
                    if len(cols) < 5:
                        continue
                    
                    # Column 0: Icon
                    icon_tag = cols[0].find('img')
                    # API results sometimes have nested attributes or direct src
                    icon_url = (icon_tag.get('data-src') or icon_tag.get('src') or "").split('/revision')[0]
                    
                    # Column 1: Name
                    name = cols[1].text.strip()
                    # Column 2: Quality
                    quality = cols[2].text.strip()
                    # Column 3: Element
                    element = cols[3].text.strip()
                    # Column 4: Weapon
                    weapon = cols[4].text.strip()
                    
                    characters.append({
                        'name': name,
                        'image_icon': icon_url,
                        'quality': quality,
                        'element': element,
                        'weapon': weapon
                    })
                
            return characters
        except Exception as e:
            print(f"Request failed: {e}")
            return []

scraper = GenshinScraper()
import time
start_time = time.time()
characters = scraper.get_character_list()
end_time = time.time()

# print(f"Scraped {len(characters)} characters in {end_time - start_time:.2f}s.")
if characters:
    print("Example character:", characters[0])


