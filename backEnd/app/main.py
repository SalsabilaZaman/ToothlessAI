from fastapi import FastAPI
from app.routers import chat

app = FastAPI(title="AI Friend")

app.include_router(chat.router)
