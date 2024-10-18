from sqlalchemy.orm import Session

from app.db_models.base import *
from app.db_models.crud.base import BaseCRUD

class TicketCRUD(BaseCRUD):
    def __init__(self, db: Session):
        super().__init__(db, Ticket)
    
    def create(self, project_id: int, title: str, description: str, status: str, priority: str):
        return super().create(project_id=project_id, title=title, description=description, status=status, priority=priority)
    
    def get(self, id: int):
        return super().get(id)
    
    def get_all(self):
        return super().get_all()
    
    def update(self, id: int, project_id: int, title: str, description: str, status: str, priority: str):
        return super().update(id, project_id=project_id, title=title, description=description, status=status, priority=priority)
    
    def delete(self, id: int):
        return super().delete(id)
