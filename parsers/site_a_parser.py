from bs4 import BeautifulSoup

from .base_parser import BaseParser


class SiteAParser(BaseParser):
    START_URL = 'https://astrakhan.su/'

    def parse_news(self, soup: BeautifulSoup):
        title = soup.find('div', class_='news-block third-style').a.get(
            'title')
        link = soup.find('div', class_='news-block third-style').a.get('href')
        soup = self.fetch_soup(link)
        img_url = soup.find('img', class_='wp-post-image')['src']

        items = {
            'title': title,
            'link': link,
            'image_url': img_url,
        }
        return items
