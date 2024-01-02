from typing import Optional, Dict

from telegram import Bot
import io
from PIL import Image


class TelegramBot:
    token = ...
    chat_id = ...
    bot = Bot(token)

    @classmethod
    def send_message(cls, message):
        cls.bot.send_message(chat_id=cls.chat_id, text=message)

    @classmethod
    def send_post(cls, image: Image, items: Optional[Dict[str, str]]) -> None:
        """Обрабатываем данные и отправляем в телеграм."""
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

        text = items.get('title') + '\n' + items.get('link')

        cls.bot.send_photo(chat_id=cls.chat_id, photo=img_byte_arr,
                           caption=text)
