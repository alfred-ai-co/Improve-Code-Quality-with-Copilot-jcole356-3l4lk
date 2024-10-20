from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class ProjectCreate(BaseModel):
    """
    ProjectCreate is a Pydantic model used for creating a new project.

    Attributes:
        name (str): The name of the project.
        description (Optional[str]): An optional description of the project. Defaults to None.
    """
    name: str
    description: Optional[str] = None


class ProjectResponse(ProjectCreate):
    """
    ProjectResponse is a Pydantic model that extends ProjectCreate and includes additional fields.
    Attributes:
        id (int): The unique identifier of the project.
        created_at (datetime): The timestamp when the project was created.
    Config:
        from_attributes (bool): Indicates that the model can be populated from attributes.
    """
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
