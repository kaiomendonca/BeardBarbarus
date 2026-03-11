from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"menssage": "BeardBarbarus API is running"}