from fastapi import FastAPI, APIRouter


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}
