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
    
    def create(self, **kwargs):
        try:
            item = self.model(**kwargs)
            self.db.add(item)
            self.db.commit()
            self.db.refresh(item)
            return item
        except SQLAlchemyError as e:
            self.db.rollback()
            logger.error(f"Error creating item: {e}")
            raise DatabaseException("Error creating item.")

    def get(self, id: int):
        try:
            item = self.db.query(self.model).filter(self.model.id == id).one()
            return item
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

    def update(self, id: int, **kwargs):
        try:
            item = self.get(id)
            for key, value in kwargs.items():
                setattr(item, key, value)
            self.db.commit()
            self.db.refresh(item)
            return item
        except ItemNotFoundException:
            raise
        except SQLAlchemyError as e:
            self.db.rollback()
            logger.error(f"Error updating item: {e}")
            raise DatabaseException("Error updating item.")

    def delete(self, id: int):
        try:
            item = self.get(id)
            self.db.delete(item)
            self.db.commit()
        except ItemNotFoundException:
            raise
        except SQLAlchemyError as e:
            self.db.rollback()
            logger.error(f"Error deleting item: {e}")
            raise DatabaseException("Error deleting item.")


class ProjectCRUD(BaseCRUD):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Project)
    
    def create(self, project: ProjectCreate):
        return super().create(**project.model_dump())
    
    def get(self, id: int):
        return super().get(id)
    
    async def get_all(self):
        return await super().get_all()
    
    def update(self, id: int, project: ProjectCreate):
        return super().update(id, **project.model_dump())
    
    def delete(self, id: int):
        return super().delete(id)


class TicketCRUD(BaseCRUD):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Ticket)
    
    def create(self, ticket: TicketCreate):
        return super().create(**ticket.model_dump())
    
    def get(self, id: int):
        return super().get(id)
    
    def get_all(self):
        return super().get_all()
    
    def update(self, id: int, ticket: TicketCreate):
        return super().update(id, **ticket.model_dump())
    
    def delete(self, id: int):
        return super().delete(id)


class KanbanBoardCRUD(BaseCRUD):
    def __init__(self, db: AsyncSession):
        super().__init__(db, KanbanBoard)
        
    def create(self, kanbanboard: KanbanBoardCreate):
        return super().create(**kanbanboard.model_dump())
    
    def get(self, id: int):
        return super().get(id)
    
    def get_all(self):
        return super().get_all()
    
    def update(self, id: int, kanbanboard: KanbanBoardUpdate) -> KanbanBoard:
        return super().update(id, **kanbanboard.model_dump())
    
    def delete(self, id: int) -> None:
        return super().delete(id)


class KanbanStatusCRUD(BaseCRUD):
    def __init__(self, db: AsyncSession):
        super().__init__(db, KanbanStatus)
    
    def create(self, kanbanstatus: KanbanStatusCreate):
        return super().create(**kanbanstatus.model_dump())
    
    def get(self, id: int):
        return super().get(id)
    
    def get_all(self):
        return super().get_all()
    
    def update(self, id: int, kanbanstatus: KanbanStatusUpdate):
        return super().update(id, **kanbanstatus.model_dump())
    
    def delete(self, id: int):
        return super().delete(id)
