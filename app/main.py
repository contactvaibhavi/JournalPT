from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from api.router import router
from dotenv import load_dotenv
from services.db_service import DbService

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Init lifespan")
    DB_SERVICE = DbService()
    DB_SERVICE.create_db()
    db = DB_SERVICE.get_db()
    yield
    print("close")

app = FastAPI(lifespan=lifespan)
app.include_router(router, prefix="/api")


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
