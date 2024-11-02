from fastapi import FastAPI
import uvicorn
from api.router import router
import urllib.parse
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy_utils import database_exists, create_database
from dotenv import load_dotenv
import os
import urllib

load_dotenv()

app = FastAPI()
app.include_router(router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


POSTGRES_USERNAME = os.getenv('POSTGRES_USERNAME')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', '')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'fastapi_rag_journal')
encoded_password = urllib.parse.quote_plus(POSTGRES_PASSWORD)

database_url = f"postgresql://{POSTGRES_USERNAME}:{encoded_password}" +\
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{DATABASE_NAME}"

engine = create_engine(database_url)

if not database_exists(engine.url):
    create_database(engine.url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()


# with engine.begin() as connection:
#     connection.execute()

try:
    Base.metadata.create_all(engine)
except Exception as e:
    print(f"Error creating tables: {e}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
