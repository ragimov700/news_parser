from abc import ABC, abstractmethod
from typing import Optional

import requests
from bs4 import BeautifulSoup


class BaseParser(ABC):
    START_URL: str = None

    def fetch_soup(self, url: str = START_URL) -> Optional[BeautifulSoup]:
        if not self.START_URL:
            raise ValueError("START_URL не определен в парсере")

        try:
            response = requests.get(self.START_URL)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except requests.RequestException as e:
            print(f'Ошибка при запросе к {url}: {e}.')
            return None

    @abstractmethod
    def parse_news(self, soup: BeautifulSoup):
        pass
