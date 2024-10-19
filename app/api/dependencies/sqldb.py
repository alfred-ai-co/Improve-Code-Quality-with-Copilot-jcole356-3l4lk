from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

from app.db_models.session import SessionLocal

# Dependency to get DB Session
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
      try:
          yield session
      finally:
          await session.close()
