from routers.schemas import PostBase
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.database import get_db
from db.models import DbPost
from datetime import datetime


def create(db: Session = Depends(get_db), request: PostBase = None):
    new_post = DbPost(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        timestamp=datetime.now(),
        user_id=request.creator_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all(db: Session = Depends(get_db)):
    return db.query(DbPost).all()


def delete(id: int, user_id: int, db: Session = Depends(get_db)):
    post = db.query(DbPost).filter(DbPost.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Post with id {id} not found')
    if post.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='Only post creator can delete post.')

    db.delete(post)
    db.commit()
    return 'ok'
