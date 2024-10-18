from sqlalchemy.orm import Session
from abc import ABC, abstractmethod

from app.db_models.crud.db import DBInterface
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
        return DBInterface(self.db,self.model).create(item)

    def get(self, id: int):
        return DBInterface(self.db,self.model).get(id)

    def get_all(self):
        return DBInterface(self.db,self.model).get_all()

    def update(self, id: int, **kwargs):
        item = self.get(id)
        for key, value in kwargs.items():
            setattr(item, key, value)
        return DBInterface(self.db,self.model).update(item)

    def delete(self, id: int):
        return DBInterface(self.db,self.model).delete(id)
