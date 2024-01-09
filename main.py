from database.dao import NewsDatabase
from image_processing.processor import ImageProcessor
from parsers.base_parser import BaseParser
from parsers.site_a_parser import SiteAParser
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
            # # Отправляем пост в телеграм
            TelegramBot.send_post(image_with_text, news_items)


def main():
    db.remove_old_news()
    site_a_parser = SiteAParser()

    run_parser(site_a_parser)


if __name__ == '__main__':
    db = NewsDatabase()

    main()
