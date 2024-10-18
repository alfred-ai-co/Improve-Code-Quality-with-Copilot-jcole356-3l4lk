from sqlalchemy.orm import Session

from app.db_models.ticket import Ticket
from app.db_models.crud.base import BaseCRUD

class TicketCRUD(BaseCRUD):
    def __init__(self, db: Session):
        super().__init__(db, Ticket)
    
    def create(self, project_id: int, title: str, description: str, status: str, priority: str, kanban_status_id: int):
        return super().create(project_id=project_id, title=title, description=description, status=status, priority=priority, kanban_status_id=kanban_status_id)
    
    def get(self, id: int):
        return super().get(id)
    
    def get_all(self):
        return super().get_all()
    
    def update(self, project_id: int, title: str, description: str, status: str, priority: str, kanban_status_id: int):
        return super().update(project_id=project_id, title=title, description=description, status=status, priority=priority, kanban_status_id=kanban_status_id)
    
    def delete(self, id: int):
        return super().delete(id)
