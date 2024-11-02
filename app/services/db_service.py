import os
import urllib.parse
from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy_utils import create_database, database_exists

POSTGRES_USERNAME = os.getenv('POSTGRES_USERNAME')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', '')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'fastapi_rag_journal')
encoded_password = urllib.parse.quote_plus(POSTGRES_PASSWORD)

database_url = f"postgresql://{POSTGRES_USERNAME}:{encoded_password}" +\
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{DATABASE_NAME}"

print(database_url)

class DbService:
    engine = None
    sessionLocal = None

    def create_db(self):
        print("create_db")
        if self.engine is None:
            self.engine = create_engine(database_url)
        
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
        
        with self.engine.begin() as connection:
            connection.execute(text('CREATE EXTENSION IF NOT EXISTS vector'))

        try:
            print(Base.metadata.tables)
            Base.metadata.create_all(self.engine)
        except Exception as e:
            print(f"Error creating tables: {e}")
    

    def get_db(self):
        if self.engine is None:
            self.create_db()
        
        sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        db = sessionLocal()

        try:
            yield db
        finally:
            db.close()
        

class Base(DeclarativeBase):
    pass

