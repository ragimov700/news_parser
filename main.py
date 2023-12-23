from parsers.site_a_parser import SiteAParser
from image_processing.processor import ImageProcessor


def run_parser(parser):
    # Получаем данные
    raw_data = parser.fetch_soup()
    news_items = parser.parse_news(raw_data)

    # Обрабатываем изображение
    image_url = news_items.get('image_url')
    ImageProcessor.download_image(image_url)


def main():
    site_a_parser = SiteAParser()

    run_parser(site_a_parser)


if __name__ == '__main__':
    main()
