from datetime import datetime, timedelta

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base, News


class NewsDatabase:
    def __init__(self, db_url='sqlite:///news.db'):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.session = sessionmaker(bind=self.engine)

    def add_news(self, title, link):
        with self.session() as session:
            new_news = News(title=title, link=link)
            session.add(new_news)
            session.commit()

    def news_exists(self, title):
        with self.session() as session:
            exists = session.query(News).filter_by(title=title).first()
            return exists

    def remove_old_news(self):
        with self.session() as session:
            threshold_date = datetime.utcnow() - timedelta(days=7)
            session.query(News).filter(News.date < threshold_date).delete()
            session.commit()
