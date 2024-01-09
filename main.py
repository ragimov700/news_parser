import time

from database.dao import NewsDatabase
from image_processing.processor import ImageProcessor
from parsers.base_parser import BaseParser
from parsers.site_a_parser import SiteAParser
from parsers.site_b_parser import SiteBParser
from parsers.site_c_parser import SiteСParser
from telegram_bot.bot import TelegramBot


def run_parser(parser: BaseParser) -> None:
    # Получаем данные
    raw_data = parser.fetch_soup()
    news_items = parser.parse_news(raw_data)
    if news_items:
        title = news_items.get('title')
        link = news_items.get('link')

        if not db.news_exists(title):
            # Добавляем новость в базу данных
            db.add_news(title, link)
            # Обрабатываем изображение
            image_url = news_items.get('image_url')
            image = ImageProcessor.download_image(image_url)
            overlay_image = ImageProcessor.image_overlay(image)
            image_with_text = ImageProcessor.add_text_to_image(
                overlay_image, news_items.get('title')
            )
            # Отправляем пост в телеграм
            TelegramBot.send_post(image_with_text, news_items)


def main(interval: int = 5) -> None:
    error_cache = None
    while True:
        try:
            site_a_parser = SiteAParser()
            site_b_parser = SiteBParser()
            site_с_parser = SiteСParser()

            run_parser(site_a_parser)
            run_parser(site_b_parser)
            run_parser(site_с_parser)
        except Exception as error:
            message = f'Сбой в работе скрипта: {error}'
            if error_cache != message:
                TelegramBot.send_message(message)
                error_cache = message
        finally:
            db.remove_old_news()
            time.sleep(interval * 60)


if __name__ == '__main__':
    db = NewsDatabase()

    main()
