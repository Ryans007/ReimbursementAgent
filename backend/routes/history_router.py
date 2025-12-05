from fastapi import APIRouter, Depends, HTTPException, Form
from database.database import get_db
from models.message_model import Message
from schemes.message_scheme import MessageScheme
from graph.graph import graph
from pydantic import BaseModel

router = APIRouter()

@router.get("/chat_history/", response_model=list[MessageScheme])
def chat_history (
    db=Depends(get_db)
):
    """Rota para obter o histórico de mensagens completo."""
    messages = db.query(Message).all()
    if not messages:
        raise HTTPException(status_code=404, detail="Thread not found")
    return messages