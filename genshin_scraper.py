import requests
from bs4 import BeautifulSoup

class GenshinScraper:
    
    def __init__(self, base_url: str = 'https://gi.yatta.moe/api/v2/en'):
        self.base_url = base_url
        self.api_url = f"{base_url}/api.php"
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

    def get_artifact_list(self):
        response = requests.get(f'{self.base_url}/reliquary')
        response.raise_for_status()
        
        artifacts = response.json()
        
        return artifacts
    
    def get_material_list(self):
        response = requests.get(f'{self.base_url}/material')
        response.raise_for_status()
        
        materials = response.json()
        
        return materials
    
    def get_material(self, material_id: int):
        response = requests.get(f'{self.base_url}/material/{material_id}')
        response.raise_for_status()
        
        material = response.json()
        
        return material
    
    def get_image(self, image_name: str):
        image_url = f"https://gi.yatta.moe/assets/UI/reliquary/{image_name}.png"
        response = requests.get(image_url)
        response.raise_for_status()
        
        
        image = response.content
        
        return image