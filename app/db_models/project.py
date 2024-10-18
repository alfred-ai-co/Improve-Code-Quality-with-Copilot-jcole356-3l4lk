from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import datetime

from app.db_models.base import Base

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    kanban_board_id = Column(Integer, ForeignKey("kanban_boards.id"), nullable=False)
    
    kanban_board = relationship("KanbanBoard", back_populates="projects")
    tickets = relationship("Ticket", back_populates="project")
