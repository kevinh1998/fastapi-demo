from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# from app.core.config import DATABASE_URL

engine = create_async_engine(
    "postgresql+asyncpg://postgres:postgres@database/postgres", echo=True
)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
