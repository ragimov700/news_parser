from typing import Dict, Optional
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from .base_parser import BaseParser


class SiteAParser(BaseParser):
    """
    Парсер для сайта новостей Астрахань.Ру.

    Этот класс наследуется от BaseParser и предоставляет
    функционал для парсинга новостей с сайта.

    :var START_URL: Начальный URL сайта для парсинга.
    """
    START_URL = 'https://astrakhan.su/'

    def parse_news(self, soup: BeautifulSoup) -> Optional[Dict[str, str]]:
        if not soup:
            return None
        # Получаем заголовок и ссылку новости:
        news_block = soup.find('div', 'news-block third-style')
        if not news_block:
            return None
        title_tag = news_block.find('a')
        if not title_tag:
            return None
        title = title_tag.get('title')
        link = urljoin(self.START_URL, title_tag.get('href'))
        # Получаем ссылку на изображение:
        soup = self.fetch_soup(link)
        image_tag = soup.find('img', 'wp-post-image')
        if not image_tag:
            return None

        image_url = image_tag.get('src')
        # Упаковываем данные в словарь:
        items = {
            'title': title,
            'link': link,
            'image_url': urljoin(self.START_URL, image_url),
        }
        return items
