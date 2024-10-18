from sqlalchemy.orm import Session

from app.db_models.kanbanstatus import KanbanStatus
from app.db_models.crud.base import BaseCRUD

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
