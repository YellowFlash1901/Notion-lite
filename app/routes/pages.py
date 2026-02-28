from fastapi import  APIRouter, status, Depends
from app.database import get_db
from app.schemas.page import CreatePage, PageResponse
from app.models.page import Page
from sqlalchemy.orm import Session


page_router = APIRouter()

@page_router.post("/create-page", response_model=PageResponse, status_code=status.HTTP_201_CREATED)
def create_page(page: CreatePage, db: Session = Depends(get_db)):
    db_page = Page(**page.dict())
    db.add(db_page)
    db.commit()
    return db_page