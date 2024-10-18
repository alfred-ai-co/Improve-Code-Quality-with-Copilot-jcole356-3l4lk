from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import datetime

from app.db_models.base import Base

class KanbanBoard(Base):
    """
    Represents a Kanban Board which contains multiple projects and statuses.
    """
    __tablename__ = "kanban_boards"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    # Relationships
    projects = relationship('Project', back_populates='kanban_board')
    statuses = relationship('KanbanStatus', back_populates='kanban_board')
