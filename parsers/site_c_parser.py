from typing import Dict, Optional
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from .base_parser import BaseParser


class SiteСParser(BaseParser):
    """
    Парсер для сайта новостей Арбуз.

    Этот класс наследуется от BaseParser и предоставляет
    функционал для парсинга новостей с сайта.

    :var START_URL: Начальный URL сайта для парсинга.
    :var base_url: URL главной страницы сайта.
    """
    START_URL = 'https://arbuztoday.ru/th/city/'
    base_url = 'https://bloknot-astrakhan.ru'

    def parse_news(self, soup: BeautifulSoup) -> Optional[Dict[str, str]]:
        if not soup:
            return None
        # Получаем заголовок и ссылку новости:
        news_block = soup.find('div', 'itemlist itemlist-prev')
        if not news_block:
            return None
        titles_block = news_block.find('div', 'itemlist__text')
        if not titles_block:
            return None
        title_tag = titles_block.find('a')
        if not title_tag:
            return None
        title = title_tag.get_text().strip()
        link = urljoin(self.base_url, title_tag.get('href'))
        # Получаем ссылку на изображение:
        soup = self.fetch_soup(link)
        image_block = soup.find('div', 'news-single-prev')
        if not image_block:
            return None
        image_tag = soup.find('img', 'wp-post-image')
        if not image_tag:
            return None
        image_url = image_tag.get('src')
        # Упаковываем данные в словарь:
        items = {
            'title': title,
            'link': link,
            'image_url': urljoin(self.base_url, image_url),
        }
        return items
