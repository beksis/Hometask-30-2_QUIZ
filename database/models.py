from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from database import Base


# Таблица для пользователей
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    phone_number = Column(Integer, nullable=False)
    level = Column(String, default='Select your level', nullable=False)
    datetime = Column(DateTime)


# Таблица вопросов
class Questions(Base):
    __tablename__ = 'questions'
    id = Column(Integer, autoincrement=True, primary_key=True)
    main_question = Column(String, nullable=False)
    v1 = Column(String)  # Змея
    v2 = Column(String)  # Язык программирования
    v3 = Column(String)  # ругань
    v4 = Column(String)  # музыкальный термин
    correct_answer = Column(Integer, nullable=False)
    timer = Column(DateTime)

# Таблица для лидеров/результатов

# Ответы пользователей на вопросы
