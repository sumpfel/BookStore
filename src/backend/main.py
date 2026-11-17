import uvicorn
from fastapi import FastAPI
from database import engine, models
from routers import books

engine.Base.metadata.create_all(bind=engine.engine)

app = FastAPI(title="mYaPP", description="mYaPP", version="1.0.0")


@app.get("/")
def root():
    return {"message":"Besuche /docs für die Swagger UI"}

app.include_router(books.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)