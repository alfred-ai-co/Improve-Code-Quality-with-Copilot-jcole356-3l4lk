from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from app.db_models.base import *


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
        item = self.model(**kwargs)
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def get(self, id: int):
        return self.db.query(self.model).filter(self.model.id == id).first()

    def get_all(self):
        return self.db.query(self.model).all()

    def update(self, id: int, **kwargs):
        item = self.get(id)
        for key, value in kwargs.items():
            setattr(item, key, value)
        self.db.commit()
        self.db.refresh(item)
        return item

    def delete(self, id: int):
        item = self.get(id)
        self.db.delete(item)
        self.db.commit()


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
