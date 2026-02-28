from fastapi import FastAPI
from app.routes.pages import page_router
from app.database import engine
from app.models.page import Base

app = FastAPI(title="Notion Lite")

Base.metadata.create_all(bind=engine)

app.include_router(page_router)

