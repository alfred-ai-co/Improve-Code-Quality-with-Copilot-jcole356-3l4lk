from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class KanbanBoardBase(BaseModel):
    """
    KanbanBoardBase is a Pydantic model representing the base structure of a Kanban board.

    Attributes:
        name (str): The name of the Kanban board.
        description (Optional[str]): An optional description of the Kanban board.
    """
    name: str
    description: Optional[str] = None


class KanbanBoardCreate(KanbanBoardBase):
    pass


class KanbanBoardUpdate(KanbanBoardBase):
    pass


class KanbanBoardInDB(KanbanBoardBase):
    """
    Represents a Kanban board stored in the database.
    Attributes:
        id (int): The unique identifier of the Kanban board.
        created_at (datetime): The timestamp when the Kanban board was created.
    Config:
        orm_mode (bool): Enables ORM mode for compatibility with ORMs like SQLAlchemy.
    """
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True


class KanbanBoardResponse(KanbanBoardInDB):
    pass
