# from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError, NoResultFound
from sqlalchemy.future import select
from abc import ABC, abstractmethod
import logging

from app.db_models.base import *
from app.api.errors.http_error import HTTPException
from app.api_models.kanbanboard import KanbanBoardCreate, KanbanBoardUpdate
from app.api_models.kanbanstatus import KanbanStatusCreate, KanbanStatusUpdate
from app.api_models.projects import ProjectCreate
from app.api_models.tickets import TicketCreate
from app.api.errors.exceptions import ItemNotFoundException, DatabaseException

logger = logging.getLogger(__name__)

class CRUDInterface(ABC):
    @abstractmethod
    def create(self, **kwargs):
        pass

    @abstractmethod
    def get(self, id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, id: int, **kwargs):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass


class BaseCRUD(CRUDInterface):
    """Base CRUD class for all models"""
    def __init__(self, db: AsyncSession, model=None):
        self.db = db
        self.model = model
    
    async def create(self, **kwargs):
        try:
            item = self.model(**kwargs)
            self.db.add(item)
            await self.db.commit()
            await self.db.refresh(item)
            return item
        except SQLAlchemyError as e:
            await self.db.rollback()
            logger.error(f"Error creating item: {e}")
            raise DatabaseException("Error creating item.")

    async def get(self, id: int):
        try:
            result = await self.db.execute(select(self.model).filter(self.model.id == id))
            return result.scalars().first()
        except NoResultFound:
            raise HTTPException(status_code=404, detail=f"Item with id {id} not found.")
        except SQLAlchemyError as e:
            logger.error(f"Error retrieving item: {e}")
            raise DatabaseException("Error retrieving item.")

    async def get_all(self):
        try:
            result = await self.db.execute(select(self.model))
            return result.scalars().all()
        except SQLAlchemyError as e:
            logger.error(f"Error retrieving items: {e}")
            raise DatabaseException("Error retrieving items.")

    async def update(self, id: int, **kwargs):
        try:
            item = await self.get(id)
            for key, value in kwargs.items():
                setattr(item, key, value)
            await self.db.commit()
            await self.db.refresh(item)
            return item
        except ItemNotFoundException:
            raise
        except SQLAlchemyError as e:
            self.db.rollback()
            logger.error(f"Error updating item: {e}")
            raise DatabaseException("Error updating item.")

    async def delete(self, id: int):
        try:
            item = await self.get(id)
            await self.db.delete(item)
            await self.db.commit()
        except ItemNotFoundException:
            raise
        except SQLAlchemyError as e:
            await self.db.rollback()
            logger.error(f"Error deleting item: {e}")
            raise DatabaseException("Error deleting item.")


class ProjectCRUD(BaseCRUD):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Project)
    
    async def create(self, project: ProjectCreate):
        return await super().create(**project.model_dump())
    
    async def get(self, id: int):
        return await super().get(id)
    
    async def get_all(self):
        return await super().get_all()
    
    async def update(self, id: int, project: ProjectCreate):
        return await super().update(id, **project.model_dump())
    
    async def delete(self, id: int):
        return await super().delete(id)


class TicketCRUD(BaseCRUD):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Ticket)
    
    async def create(self, ticket: TicketCreate):
        return await super().create(**ticket.model_dump())
    
    async def get(self, id: int):
        return await super().get(id)
    
    async def get_all(self):
        return await super().get_all()
    
    async def update(self, id: int, ticket: TicketCreate):
        return await super().update(id, **ticket.model_dump())
    
    async def delete(self, id: int):
        return await super().delete(id)


class KanbanBoardCRUD(BaseCRUD):
    def __init__(self, db: AsyncSession):
        super().__init__(db, KanbanBoard)
        
    async def create(self, kanbanboard: KanbanBoardCreate):
        return await super().create(**kanbanboard.model_dump())
    
    async def get(self, id: int):
        return await super().get(id)
    
    async def get_all(self):
        return await super().get_all()
    
    async def update(self, id: int, kanbanboard: KanbanBoardUpdate):
        return await super().update(id, **kanbanboard.model_dump())
    
    async def delete(self, id: int):
        return await super().delete(id)


class KanbanStatusCRUD(BaseCRUD):
    def __init__(self, db: AsyncSession):
        super().__init__(db, KanbanStatus)
    
    async def create(self, kanbanstatus: KanbanStatusCreate):
        return await super().create(**kanbanstatus.model_dump())
    
    async def get(self, id: int):
        return await super().get(id)
    
    async def get_all(self):
        return await super().get_all()
    
    async def update(self, id: int, kanbanstatus: KanbanStatusUpdate):
        return await super().update(id, **kanbanstatus.model_dump())
    
    async def delete(self, id: int):
        return await super().delete(id)
