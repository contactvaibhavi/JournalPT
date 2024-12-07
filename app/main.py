from fastapi import FastAPI
import uvicorn
from api.router import router
from dotenv import load_dotenv


load_dotenv()

app = FastAPI()
app.include_router(router, prefix="/api")


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
