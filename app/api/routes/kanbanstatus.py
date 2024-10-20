from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends

from app.db_models.crud import KanbanStatusCRUD
from app.api_models.kanbanstatus import KanbanStatusCreate, KanbanStatusResponse
from app.api.dependencies.sqldb import get_db

# Create a new APIRouter instance for Kanban status-related routes
router = APIRouter()

@router.post("/", status_code=201, response_model=KanbanStatusResponse)
def create_kanban_status(kanban_status: KanbanStatusCreate, db: Session = Depends(get_db)):
    """
    Create a new Kanban status.

    :param kanban_status: KanbanStatusCreate - Pydantic model containing Kanban status data
    :param db: Session - SQLAlchemy session dependency
    :return: KanbanStatusResponse - Pydantic model containing the created Kanban status data
    """
    kanban_status_crud = KanbanStatusCRUD(db)
    return kanban_status_crud.create(**kanban_status.model_dump())

@router.get("/", status_code=200, response_model=list[KanbanStatusResponse])
def get_all_kanban_statuses(db: Session = Depends(get_db)):
    """
    Retrieve all Kanban statuses.

    :param db: Session - SQLAlchemy session dependency
    :return: List[KanbanStatusResponse] - List of Pydantic models containing Kanban status data
    """
    kanban_status_crud = KanbanStatusCRUD(db)
    return kanban_status_crud.get_all()

@router.get("/{id}", status_code=200, response_model=KanbanStatusResponse)
def get_kanban_status(id: int, db: Session = Depends(get_db)):
    """
    Retrieve a Kanban status by its ID.

    :param id: int - Kanban status ID
    :param db: Session - SQLAlchemy session dependency
    :return: KanbanStatusResponse - Pydantic model containing the Kanban status data
    :raises HTTPException: If the Kanban status with the given ID is not found
    """
    kanban_status_crud = KanbanStatusCRUD(db)
    kanban_status = kanban_status_crud.get(id)
    if not kanban_status:
        raise HTTPException(status_code=404, detail=f"Kanban Status with id {id} not found")
    return kanban_status

@router.put("/{id}", status_code=200, response_model=KanbanStatusResponse)
def update_kanban_status(id: int, kanban_status: KanbanStatusCreate, db: Session = Depends(get_db)):
    """
    Update a Kanban status by its ID.

    :param id: int - Kanban status ID
    :param kanban_status: KanbanStatusCreate - Pydantic model containing updated Kanban status data
    :param db: Session - SQLAlchemy session dependency
    :return: KanbanStatusResponse - Pydantic model containing the updated Kanban status data
    """
    kanban_status_crud = KanbanStatusCRUD(db)
    kanban_status_crud.update(id, **kanban_status.model_dump())
    return kanban_status_crud.get(id)

@router.delete("/{id}", status_code=204)
def delete_kanban_status(id: int, db: Session = Depends(get_db)):
    """
    Delete a Kanban status by its ID.

    :param id: int - Kanban status ID
    :param db: Session - SQLAlchemy session dependency
    :return: dict - Message indicating successful deletion
    """
    kanban_status_crud = KanbanStatusCRUD(db)
    kanban_status_crud.delete(id)
    return {"message": "Kanban Status deleted successfully"}
