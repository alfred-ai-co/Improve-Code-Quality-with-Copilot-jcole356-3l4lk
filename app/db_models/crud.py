from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, NoResultFound
from abc import ABC, abstractmethod
import logging

from app.db_models.base import *
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
    def __init__(self, db: Session, model=None):
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
            logger.error(f"Item with id {id} not found.")
            raise ItemNotFoundException(id)
        except SQLAlchemyError as e:
            logger.error(f"Error retrieving item: {e}")
            raise DatabaseException("Error retrieving item.")

    def get_all(self):
        try:
            return self.db.query(self.model).all()
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
    def __init__(self, db: Session):
        super().__init__(db, Project)
    
    def create(self, name: str, description: str, kanban_board_id: int):
        return super().create(name=name, description=description, kanban_board_id=kanban_board_id)
    
    def get(self, id: int):
        return super().get(id)
    
    def get_all(self):
        return super().get_all()
    
    def update(self, id: int, name: str, description: str, kanban_board_id: int):
        return super().update(id, name=name, description=description, kanban_board_id=kanban_board_id)
    
    def delete(self, id: int):
        return super().delete(id)


class TicketCRUD(BaseCRUD):
    def __init__(self, db: Session):
        super().__init__(db, Ticket)
    
    def create(self, ticket: TicketCreate):
        return super().create(**ticket.model_dump())
    
    def get(self, id: int):
        return super().get(id)
    
    def get_all(self):
        return super().get_all()
    
    def update(self, id: int, project_id: int, title: str, description: str, status: str, priority: str, kanban_status_id: int):
        return super().update(id, project_id=project_id, title=title, description=description, status=status, priority=priority, kanban_status_id=kanban_status_id)
    
    def delete(self, id: int):
        return super().delete(id)


class KanbanBoardCRUD(BaseCRUD):
    def __init__(self, db: Session):
        super().__init__(db, KanbanBoard)
        
    def create(self, name: str, description: str):
        return super().create(name=name, description=description)
    
    def get(self, id: int):
        return super().get(id)
    
    def get_all(self):
        return super().get_all()
    
    def update(self, id: int, name: str, description: str) -> KanbanBoard:
        return super().update(id, name=name, description=description)
    
    def delete(self, id: int) -> None:
        return super().delete(id)


class KanbanStatusCRUD(BaseCRUD):
    def __init__(self, db: Session):
        super().__init__(db, KanbanStatus)
    
    def create(self, name: str, description: str, board_id: int):
        return super().create(name=name, description=description, board_id=board_id)
    
    def get(self, id: int):
        return super().get(id)
    
    def get_all(self):
        return super().get_all()
    
    def update(self, id: int, name: str, description: str, board_id: int):
        return super().update(id, name=name, description=description, board_id=board_id)
    
    def delete(self, id: int):
        return super().delete(id)