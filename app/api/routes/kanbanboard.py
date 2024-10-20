from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends

from app.db_models.crud import KanbanBoardCRUD, KanbanStatusCRUD
from app.api_models.kanbanboard import KanbanBoardCreate, KanbanBoardResponse
from app.api.dependencies.sqldb import get_db

# Create a new APIRouter instance for Kanban board-related routes
router = APIRouter()

@router.post("/", status_code=201, response_model=KanbanBoardResponse)
def create_kanban_board(kanban_board: KanbanBoardCreate, db: Session = Depends(get_db)):
    """
    Create a new Kanban board.

    :param kanban_board: KanbanBoardCreate - Pydantic model containing Kanban board data
    :param db: Session - SQLAlchemy session dependency
    :return: KanbanBoardResponse - Pydantic model containing the created Kanban board data
    """
    kanban_board_crud = KanbanBoardCRUD(db)
    return kanban_board_crud.create(**kanban_board.model_dump())

@router.get("/", status_code=200, response_model=list[KanbanBoardResponse])
def get_all_kanban_boards(db: Session = Depends(get_db)):
    """
    Retrieve all Kanban boards.

    :param db: Session - SQLAlchemy session dependency
    :return: List[KanbanBoardResponse] - List of Pydantic models containing Kanban board data
    """
    kanban_board_crud = KanbanBoardCRUD(db)
    return kanban_board_crud.get_all()

@router.get("/{id}", status_code=200, response_model=KanbanBoardResponse)
def get_kanban_board(id: int, db: Session = Depends(get_db)):
    """
    Retrieve a Kanban board by its ID.

    :param id: int - Kanban board ID
    :param db: Session - SQLAlchemy session dependency
    :return: KanbanBoardResponse - Pydantic model containing the Kanban board data
    :raises HTTPException: If the Kanban board with the given ID is not found
    """
    kanban_board_crud = KanbanBoardCRUD(db)
    kanban_board = kanban_board_crud.get(id)
    if not kanban_board:
        raise HTTPException(status_code=404, detail=f"Kanban Board with id {id} not found")
    return kanban_board

@router.put("/{id}", status_code=200, response_model=KanbanBoardResponse)
def update_kanban_board(id: int, kanban_board: KanbanBoardCreate, db: Session = Depends(get_db)):
    """
    Update a Kanban board by its ID.

    :param id: int - Kanban board ID
    :param kanban_board: KanbanBoardCreate - Pydantic model containing updated Kanban board data
    :param db: Session - SQLAlchemy session dependency
    :return: KanbanBoardResponse - Pydantic model containing the updated Kanban board data
    """
    kanban_board_crud = KanbanBoardCRUD(db)
    kanban_board_crud.update(id, **kanban_board.model_dump())
    return kanban_board_crud.get(id)

@router.delete("/{id}", status_code=204)
def delete_kanban_board(id: int, db: Session = Depends(get_db)):
    """
    Delete a Kanban board by its ID.

    :param id: int - Kanban board ID
    :param db: Session - SQLAlchemy session dependency
    :return: dict - Message indicating successful deletion
    """
    kanban_board_crud = KanbanBoardCRUD(db)
    kanban_board_crud.delete(id)
    return {"message": "Kanban Board deleted successfully"}
