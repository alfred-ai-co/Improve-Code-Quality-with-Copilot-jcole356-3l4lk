from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class TicketCreate(BaseModel):
    """
    TicketCreate is a Pydantic model representing the data required to create a new ticket.

    Attributes:
        project_id (int): The ID of the project to which the ticket belongs.
        title (str): The title of the ticket.
        description (str): A detailed description of the ticket.
        status (str): The current status of the ticket.
        priority (str): The priority level of the ticket.
    """
    project_id: int
    title: str
    description: str
    status: str
    priority: str


class TicketResponse(TicketCreate):
    """
    TicketResponse model extends TicketCreate and includes additional fields.
    Attributes:
        id (int): Unique identifier for the ticket.
        created_at (datetime): Timestamp when the ticket was created.
    Config:
        from_attributes (bool): Configuration to enable attribute-based initialization.
    """
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
