from parsers.site_a_parser import SiteAParser
from parsers.base_parser import BaseParser
from image_processing.processor import ImageProcessor


def run_parser(parser: BaseParser) -> ...:
    # Получаем данные
    raw_data = parser.fetch_soup()
    news_items = parser.parse_news(raw_data)
    if news_items:
        # Обрабатываем изображение
        image_url = news_items.get('image_url')
        image = ImageProcessor.download_image(image_url)
        overlay_image = ImageProcessor.image_overlay(image)
        # overlay_image.show()
        image_with_text = ImageProcessor.add_text_to_image(overlay_image, news_items.get('title'))
        image_with_text.show()
    # return parser


def main():
    site_a_parser = SiteAParser()

    run_parser(site_a_parser)


if __name__ == '__main__':
    main()
