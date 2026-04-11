from bs4 import BeautifulSoup
import requests

class GenshinScraper:
    
    def __init__(self, base_url: str = 'https://game8.co/games/Genshin-Impact'):
        self.base_url = base_url
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"

    def get_character_list(self):
        pass