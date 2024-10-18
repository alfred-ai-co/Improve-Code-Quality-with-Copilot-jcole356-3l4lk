from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import datetime

from app.db_models.base import Base

class KanbanStatus(Base):
    """
    Represents a status within a Kanban Board, such as 'To Do', 'In Progress', or 'Done'.
    """
    __tablename__ = "kanban_statuses"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    board_id = Column(Integer, ForeignKey("kanban_boards.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    
    # Relationships
    kanban_board = relationship('KanbanBoard', back_populates='statuses')
    tickets = relationship('Ticket', back_populates='kanban_status')
