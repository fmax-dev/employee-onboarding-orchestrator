from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlmodel.ext.asyncio import AsyncSession  # pyright: ignore[reportMissingImports]

from backend.app.core.config import settings

engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=True
)

async_session_local = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_session():
    async with async_session_local() as session:
        yield session

