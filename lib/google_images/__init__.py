import requests
from bs4 import BeautifulSoup


class Image:

    def __init__(self, search_term):
        self.search_term = search_term
        self.search_url = f'https://www.google.com/images?q={self.search_term}'
        self.all_links = self.get_image_links()
        self.link = self.all_links[0]

    def __repr__(self):
        return f"Image('{self.search_term}')"

    def __str__(self):
        return self.link

    def get_image_links(self):
        html = requests.get(self.search_url).text
        soup = BeautifulSoup(html, 'html.parser')
        links = (img.get('src') for img in soup.find_all('img') if img.get('src'))
        return [link for link in links if 'http' in link]
