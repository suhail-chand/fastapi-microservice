from fastapi import FastAPI
from app.db import Base, engine
from app.routers import users

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI microservice!"}