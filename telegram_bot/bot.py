import io
import os
from typing import Optional, Dict

from PIL import Image
from dotenv import load_dotenv
from telegram import Bot

load_dotenv()


class TelegramBot:
    token = os.getenv('TOKEN')
    chat_id = os.getenv('CHAT_ID')
    bot = Bot(token)

    @classmethod
    def send_message(cls, message):
        """Отправляем пост в телеграм"""
        cls.bot.send_message(chat_id=cls.chat_id, text=message)

    @classmethod
    def send_post(cls, image: Image, items: Optional[Dict[str, str]]) -> None:
        """Отправляем пост телеграм."""
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

        text = items.get('title') + '\n' + items.get('link')

        cls.bot.send_photo(chat_id=cls.chat_id, photo=img_byte_arr,
                           caption=text)
