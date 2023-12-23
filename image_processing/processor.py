from io import BytesIO

import requests
from PIL import Image


class ImageProcessor:
    """
    Класс для обработки изображений, извлеченных из новостных статей.
    """

    @staticmethod
    def download_image(image_url: str) -> Image:
        """
        Загружает изображение по URL.

        :param image_url: URL изображения для загрузки.
        :return: Объект изображения PIL.
        """
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        return image
