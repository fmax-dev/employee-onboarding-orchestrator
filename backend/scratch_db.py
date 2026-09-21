import asyncio

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.core.config import settings
from app.db.session import engine


async def test_database_connection():
    print("Connecting to db...")

    try:
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT 1"))
            print("\n" + "=" * 30)
            print(f"Successfully connected to {settings.POSTGRES_DB}!")
            print("Query Result:", result.scalar_one())
            print("=" * 30)
    except SQLAlchemyError as e:
        print(f"\nDatabase connection failed: {e}\n")


if __name__ == "__main__":
    asyncio.run(test_database_connection())
