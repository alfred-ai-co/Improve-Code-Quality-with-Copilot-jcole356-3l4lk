from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

from app.db_models.session import SessionLocal

# Dependency to get DB Session
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as db:
      try:
          yield db
      finally:
          await db.close()
