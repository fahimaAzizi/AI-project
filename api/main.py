from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from app.routes import bug_routes
from app.config import settings

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)

app.include_router(bug_routes.router)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
