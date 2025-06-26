from config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
import os

class Database:
    def __init__(self, echo=True):
        self.db_path = Config.DB_PATH
        self.db_url = 'sqlite:///' + self.db_path
        self.echo = echo
        self.__ensure_db()

        self.engine = create_engine(self.db_url, echo=self.echo)
        self.SessionLocal = scoped_session(sessionmaker(bind=self.engine))
        self.Base = declarative_base()
    
    def __ensure_db(self):
        # Garante que o diretório onde o banco será salvo exista
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        print(f"Create database at <'{self.db_path}'>")
        print(f'BASE_DIR={Config.BASE_DIR}')
    
    def get_session(self):
        return self.SessionLocal()
    
    def init_db(self):
        # Importa os modelos aqui para registrar com o metadata
        from models import employee  # Adicione outros modelos se necessário
        self.Base.metadata.create_all(bind=self.engine)


db = Database()
