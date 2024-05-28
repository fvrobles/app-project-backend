from fastapi import FastAPI

app = FastAPI()

@app.get("/api/title")
def read_root():
    return {"title": "World!"}
