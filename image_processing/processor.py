from io import BytesIO

import requests
from PIL import Image, ImageDraw, ImageFont


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

    @staticmethod
    def image_overlay(image: Image) -> Image:
        """Наложение рамки на изображение."""
        overlay = Image.open('image_processing/templates/overlay.PNG')
        width, height = image.size
        size = min(width, height)
        square_img = Image.new('RGB', (size, size), 'white')
        offset_x = (size - width) // 2
        offset_y = (size - height) // 2
        square_img.paste(image, (offset_x, offset_y))
        resized_img = square_img.resize((1500, 1500))
        resized_img.paste(overlay, (0, 0), overlay)
        return resized_img

    @staticmethod
    def add_text_to_image(image: Image, text: str, max_len: int = 25) -> Image:
        """Форматирование и наложение текста на изображение."""
        words = text.upper().split()
        lines = []
        current_line = []
        for word in words:
            if len(' '.join(current_line + [word])) > max_len:
                lines.append(' '.join(current_line))
                current_line = [word]
            else:
                current_line.append(word)
        lines.append(' '.join(current_line))
        wrapped_text = '\n'.join(lines)

        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(
            'image_processing/fonts/Montserrat-Bold.ttf', size=70
        )
        text_bbox = draw.textbbox((0, 0), wrapped_text, font=font)
        text_width, text_height = (text_bbox[2] - text_bbox[0],
                                   text_bbox[3] - text_bbox[1])
        text_x = (1500 - text_width) / 2
        text_y = 1500 - text_height - 100
        draw.text((text_x, text_y), wrapped_text, font=font, fill="white")
        return image
