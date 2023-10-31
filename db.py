from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Float, DateTime
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy import inspect
import logging
# import os

username = 'postgres'
password = 'gfhjkm'
db_name = 'hw07'
domain = 'localhost' 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG)
sqlalchemy_logger = logging.getLogger('sqlalchemy')
sqlalchemy_logger.setLevel(logging.DEBUG)

try:
    url = f'postgresql://{username}:{password}@{domain}:5432/{db_name}'
    # url = ('postgresql://postgres:gfhjkm@localhost:5432/hw0007') #ArgumentError: Could not parse SQLAlchemy URL from string 
    # password = os.getenv('gfhjkm')
    # url = f'postgre://{username}:{password}@{domain}:5432/{db_name}' 
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()
    logging.debug(f"Спроба створення з'єднання з URL: {url}")

    logger.info("Підключено до бази даних PostgreSQL")
    inspector = inspect(engine)
    # Отримайте список таблиц у базі даних
    tables = inspector.get_table_names()
    logger.info(f"Список таблиц у базі даних: {tables}")

    session.close()

except Exception as e:
    logger.error(f"Помилка при підключенні до бази даних: {str(e)}")
