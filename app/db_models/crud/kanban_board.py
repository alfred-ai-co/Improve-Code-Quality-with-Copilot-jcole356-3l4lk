from sqlalchemy.orm import Session

from app.db_models.kanban_board import KanbanBoard
from app.db_models.crud.base import BaseCRUD

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
