from datetime import datetime, timedelta

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base, News


class NewsDatabase:
    """
    Класс для работы с базой данных.

    Этот класс предоставляет методы для добавления новостей,
    проверки наличия новостей в базе данных и удаления устаревших новостей.

    :param db_url: Строка подключения к базе данных.
    """
    def __init__(self, db_url='sqlite:///news.db'):
        """
        Инициализация базы данных.
        """
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.session = sessionmaker(bind=self.engine)

    def add_news(self, title, link):
        """
        Добавляет новость в базу данных.

        :param title: Заголовок новости.
        :param link: Ссылка на новость.
        """
        with self.session() as session:
            new_news = News(title=title, link=link)
            session.add(new_news)
            session.commit()

    def news_exists(self, title):
        """
        Проверяет, существует ли новость с заданным заголовком в базе данных.

        :param title: Заголовок новости для проверки.
        :return: Возвращает True, если новость существует, иначе False.
        """
        with self.session() as session:
            exists = session.query(News).filter_by(title=title).first()
            return bool(exists)

    def remove_old_news(self):
        """
        Удаляет новости, которым больше 7 дней с момента их добавления.
        """
        with self.session() as session:
            threshold_date = datetime.utcnow() - timedelta(days=7)
            session.query(News).filter(News.date < threshold_date).delete()
            session.commit()
