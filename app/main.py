from fastapi import FastAPI
from app.database.connection import test_connection

app = FastAPI()

@app.get("/")
def read_root():
    return {"menssage": "BeardBarbarus API is running"}

@app.get("/test-db")
def test_db():
    result = test_connection()
    return {"database": "connected", "result": result}