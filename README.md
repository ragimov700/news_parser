<h1 align="center">News Parser</h1>

News Parser - это проект для автоматического сбора новостей с различных сайтов, обработки изображений из этих новостей и публикации их в Telegram. Проект включает в себя модули для парсинга сайтов, обработки изображений и взаимодействия с Telegram.



---
### Технологии
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-3776AB?style=for-the-badge)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-CC2927?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-7B68EE?style=for-the-badge)
![Telegram Bot API](https://img.shields.io/badge/Telegram_Bot_API-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Poetry](https://img.shields.io/badge/Poetry-60A5FA?style=for-the-badge&logo=python&logoColor=white)

### Как это работает
- Скрипт периодически запрашивает новости с различных сайтов.
- Для каждой новости проверяется, была ли она уже добавлена в базу данных.
- Если новость новая, она добавляется в базу данных.
- Для каждой новой новости обрабатывается изображение (например, добавляется текстовая накладка).
- Обработанное изображение вместе с информацией о новости отправляется в Telegram.
---
<details>
  <summary>Нажмите, чтобы увидеть скриншот</summary>
  
  ![Скриншот 1](https://drive.google.com/uc?export=view&id=14GgSzII1UCvWoEUpVNIYOX9PgzilpN4L)

</details>

# Установка
### 1. Клонируем репозиторий
```
git clone git@github.com:ragimov700/Foodgram.git
```
### 2. Создаем .env файл в корневой директории
```
TOKEN= # Токен телеграм бота
CHAT_ID= # chat_id телеграм чата
```
### 3. Запускаем Докер в корневой директории
```
sudo docker compose up -d
```
---
<h5 align="center">Автор проекта: <a href="https://github.com/ragimov700">Sherif Ragimov</a></h5>
