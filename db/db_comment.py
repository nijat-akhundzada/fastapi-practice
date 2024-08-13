from sqlalchemy.orm import Session
from db.database import get_db
from fastapi import Depends
from db.models import DbComment
from routers.schemas import CommentBase
from datetime import datetime


def create(request: CommentBase, db: Session = Depends(get_db)):
    new_comment = DbComment(
        text=request.text,
        username=request.username,
        post_id=request.post_id,
        timestamp=datetime.now()
    )

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def get_all(post_id: int, db: Session = Depends(get_db)):
    return db.query(DbComment).filter(DbComment.post_id == post_id).all()
