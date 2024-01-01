from abc import ABC, abstractmethod
from typing import Optional, Dict

import requests
from bs4 import BeautifulSoup


class BaseParser(ABC):
    START_URL: str = None
    HEADERS = {'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    )
    }

    def fetch_soup(self, url: Optional[str] = None) -> Optional[BeautifulSoup]:
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
        pass
