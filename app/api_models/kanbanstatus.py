from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class KanbanStatusBase(BaseModel):
    """
    KanbanStatusBase is a Pydantic model that represents the base schema for a Kanban status.

    Attributes:
        name (str): The name of the Kanban status.
        description (Optional[str]): An optional description of the Kanban status. Defaults to None.
        board_id (int): The ID of the board to which the Kanban status belongs.
    """
    name: str
    description: Optional[str] = None
    board_id: int


class KanbanStatusCreate(KanbanStatusBase):
    pass


class KanbanStatusUpdate(KanbanStatusBase):
    pass


class KanbanStatusInDB(KanbanStatusBase):
    """
    KanbanStatusInDB represents a Kanban status entity stored in the database.
    Attributes:
        id (int): The unique identifier of the Kanban status.
        created_at (datetime): The timestamp when the Kanban status was created.
    Config:
        orm_mode (bool): Enables ORM mode for compatibility with ORMs like SQLAlchemy.
    """
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True


class KanbanStatusResponse(KanbanStatusInDB):
    pass
