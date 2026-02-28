import uuid
from fastapi import  FastAPI, status, Depends
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import get_db


Base = declarative_base()


class Page(Base):
    __tablename__ = "pages"
    id    = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String)
    content = Column(String)

# Base.metadata.create_all(bind=engine)


app = FastAPI()


class Pagebase(BaseModel):
    title : str
    content: str

class CreatePage(Pagebase):
    pass

class PageResponse(Pagebase):
    pass

@app.post("/create-page", response_model=PageResponse, status_code=status.HTTP_201_CREATED)
async def create_page(page: CreatePage, db: Session = Depends(get_db)):
    db_page = Page(**page.dict())
    db.add(db_page)
    db.commit()
    return db_page

