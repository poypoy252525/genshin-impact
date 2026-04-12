from bs4 import BeautifulSoup
import requests

class GenshinScraper:
    
    def __init__(self, base_url: str = 'https://genshin-impact.fandom.com/wiki/'):
        self.base_url = base_url
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"

    def get_character_list(self):
        response  = requests.get(f'{self.base_url}/Character/List', headers={'User-Agent': self.user_agent})
        soup = BeautifulSoup(response.content, 'html.parser')
        
        items = soup.select('table.fandom-table > tbody > tr')

        characters = []

        for item in items:
            characters.append(
                {
                    'image_icon': item.select_one('td > span[typeof="mw:File"] > a > img').attrs["data-src"],
                }
            )