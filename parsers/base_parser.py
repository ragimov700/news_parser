from abc import ABC, abstractmethod
from typing import Dict, Optional

import requests
from bs4 import BeautifulSoup


class BaseParser(ABC):
    """
    Абстрактный базовый класс для парсеров сайтов.

    Определяет общие свойства и методы для дочерних парсеров.

    :var START_URL: Начальный URL. Должен быть определён в дочерних классах.
    :var HEADERS: Заголовки HTTP-запросов для имитации запросов от браузера.
    """
    START_URL: str = None
    HEADERS = {'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    )
    }

    def fetch_soup(self, url: Optional[str] = None) -> Optional[BeautifulSoup]:
        """
        Отправляет запрос к заданному URL и возвращает объект BeautifulSoup.

        Если URL не указан, используется START_URL класса.

        :param url: URL для запроса. Если None, используется START_URL.
        :return: Объект BeautifulSoup, созданный из HTML-контента ответа.
        """
        if not self.START_URL:
            raise ValueError("START_URL не определен в парсере.")
        if url is None:
            url = self.START_URL
        try:
            response = requests.get(url, headers=self.HEADERS)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'lxml')
        except requests.RequestException as e:
            print(f'Ошибка при запросе к {url}: {e}.')
            return None

    @abstractmethod
    def parse_news(self, soup: BeautifulSoup) -> Optional[Dict[str, str]]:
        """
        Абстрактный метод для парсинга новостей.

        Должен быть реализован в дочерних классах.

        :param soup: Объект BeautifulSoup, содержащий HTML-контент страницы.
        :return: Словарь с данными новости.
        """
        pass
