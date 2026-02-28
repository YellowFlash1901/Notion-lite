from app.config import Settings
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine


settings = Settings()
engine = create_engine(settings.DATABASE_URL, echo=False)
SessionLocal = sessionmaker(engine)


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
