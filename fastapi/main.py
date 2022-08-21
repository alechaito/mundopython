


# pip install fastapi
# apt install uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# http://127.0.0.1:8000
# http://127.0.0.1:8000/docs
