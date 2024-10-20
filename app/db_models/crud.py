from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from app.db_models.base import *

# Abstract base class defining the CRUD interface
class CRUDInterface(ABC):
    @abstractmethod
    def create(self, **kwargs):
        """Create a new item"""
        pass

    @abstractmethod
    def get(self, id: int):
        """Retrieve an item by its ID"""
        pass

    @abstractmethod
    def get_all(self):
        """Retrieve all items"""
        pass

    @abstractmethod
    def update(self, id: int, **kwargs):
        """Update an item by its ID"""
        pass

    @abstractmethod
    def delete(self, id: int):
        """Delete an item by its ID"""
        pass

# Base CRUD class implementing the CRUD interface
class BaseCRUD(CRUDInterface):
    """Base CRUD class for all models"""
    def __init__(self, db: Session, model=None):
        """
        Initialize the BaseCRUD class.

        :param db: SQLAlchemy session
        :param model: SQLAlchemy model class
        """
        self.db = db
        self.model = model
    
    def create(self, **kwargs):
        """
        Create a new item.

        :param kwargs: Item attributes
        :return: Created item
        """
        item = self.model(**kwargs)
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def get(self, id: int):
        """
        Retrieve an item by its ID.

        :param id: Item ID
        :return: Retrieved item
        """
        return self.db.query(self.model).filter(self.model.id == id).first()

    def get_all(self):
        """
        Retrieve all items.

        :return: List of all items
        """
        return self.db.query(self.model).all()

    def update(self, id: int, **kwargs):
        """
        Update an item by its ID.

        :param id: Item ID
        :param kwargs: Updated attributes
        :return: Updated item
        """
        item = self.get(id)
        for key, value in kwargs.items():
            setattr(item, key, value)
        self.db.commit()
        self.db.refresh(item)
        return item

    def delete(self, id: int):
        """
        Delete an item by its ID.

        :param id: Item ID
        """
        item = self.get(id)
        self.db.delete(item)
        self.db.commit()

# CRUD class for Project model
class ProjectCRUD(BaseCRUD):
    def __init__(self, db: Session):
        """
        Initialize the ProjectCRUD class.

        :param db: SQLAlchemy session
        """
        super().__init__(db, Project)
    
    def create(self, name: str, description: str):
        """
        Create a new project.

        :param name: Project name
        :param description: Project description
        :return: Created project
        """
        return super().create(name=name, description=description)
    
    def get(self, id: int):
        """
        Retrieve a project by its ID.

        :param id: Project ID
        :return: Retrieved project
        """
        return super().get(id)
    
    def get_all(self):
        """
        Retrieve all projects.

        :return: List of all projects
        """
        return super().get_all()
    
    def update(self, id: int, name: str, description: str):
        """
        Update a project by its ID.

        :param id: Project ID
        :param name: Project name
        :param description: Project description
        :return: Updated project
        """
        return super().update(id, name=name, description=description)
    
    def delete(self, id: int):
        """
        Delete a project by its ID.

        :param id: Project ID
        """
        return super().delete(id)

# CRUD class for Ticket model
class TicketCRUD(BaseCRUD):
    def __init__(self, db: Session):
        """
        Initialize the TicketCRUD class.

        :param db: SQLAlchemy session
        """
        super().__init__(db, Ticket)
    
    def create(self, project_id: int, title: str, description: str, status: str, priority: str):
        """
        Create a new ticket.

        :param project_id: Project ID
        :param title: Ticket title
        :param description: Ticket description
        :param status: Ticket status
        :param priority: Ticket priority
        :return: Created ticket
        """
        return super().create(project_id=project_id, title=title, description=description, status=status, priority=priority)
    
    def get(self, id: int):
        """
        Retrieve a ticket by its ID.

        :param id: Ticket ID
        :return: Retrieved ticket
        """
        return super().get(id)
    
    def get_all(self):
        """
        Retrieve all tickets.

        :return: List of all tickets
        """
        return super().get_all()
    
    def update(self, id: int, project_id: int, title: str, description: str, status: str, priority: str):
        """
        Update a ticket by its ID.

        :param id: Ticket ID
        :param project_id: Project ID
        :param title: Ticket title
        :param description: Ticket description
        :param status: Ticket status
        :param priority: Ticket priority
        :return: Updated ticket
        """
        return super().update(id, project_id=project_id, title=title, description=description, status=status, priority=priority)
    
    def delete(self, id: int):
        """
        Delete a ticket by its ID.

        :param id: Ticket ID
        """
        return super().delete(id)

# CRUD class for KanbanBoard model
class KanbanBoardCRUD(BaseCRUD):
    def __init__(self, db: Session):
        """
        Initialize the KanbanBoardCRUD class.

        :param db: SQLAlchemy session
        """
        super().__init__(db, KanbanBoard)
        
    def create(self, name: str, description: str):
        """
        Create a new Kanban board.

        :param name: Kanban board name
        :param description: Kanban board description
        :return: Created Kanban board
        """
        return super().create(name=name, description=description)
    
    def get(self, id: int):
        """
        Retrieve a Kanban board by its ID.

        :param id: Kanban board ID
        :return: Retrieved Kanban board
        """
        return super().get(id)
    
    def get_all(self):
        """
        Retrieve all Kanban boards.

        :return: List of all Kanban boards
        """
        return super().get_all()
    
    def update(self, id: int, name: str, description: str) -> KanbanBoard:
        """
        Update a Kanban board by its ID.

        :param id: Kanban board ID
        :param name: Kanban board name
        :param description: Kanban board description
        :return: Updated Kanban board
        """
        return super().update(id, name=name, description=description)
    
    def delete(self, id: int) -> None:
        """
        Delete a Kanban board by its ID.

        :param id: Kanban board ID
        """
        return super().delete(id)

# CRUD class for KanbanStatus model
class KanbanStatusCRUD(BaseCRUD):
    def __init__(self, db: Session):
        """
        Initialize the KanbanStatusCRUD class.

        :param db: SQLAlchemy session
        """
        super().__init__(db, KanbanStatus)
    
    def create(self, name: str, description: str, board_id: int):
        """
        Create a new Kanban status.

        :param name: Kanban status name
        :param description: Kanban status description
        :param board_id: Kanban board ID
        :return: Created Kanban status
        """
        return super().create(name=name, description=description, board_id=board_id)
    
    def get(self, id: int):
        """
        Retrieve a Kanban status by its ID.

        :param id: Kanban status ID
        :return: Retrieved Kanban status
        """
        return super().get(id)
    
    def get_all(self):
        """
        Retrieve all Kanban statuses.

        :return: List of all Kanban statuses
        """
        return super().get_all()
    
    def update(self, id: int, name: str, description: str, board_id: int):
        """
        Update a Kanban status by its ID.

        :param id: Kanban status ID
        :param name: Kanban status name
        :param description: Kanban status description
        :param board_id: Kanban board ID
        :return: Updated Kanban status
        """
        return super().update(id, name=name, description=description, board_id=board_id)
    
    def delete(self, id: int):
        """
        Delete a Kanban status by its ID.

        :param id: Kanban status ID
        """
        return super().delete(id)
