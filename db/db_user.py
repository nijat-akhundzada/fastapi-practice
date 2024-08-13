from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from db.database import get_db
from routers.schemas import UserBase
from db.models import DbUser
from db.hashing import Hash


def create_user(db: Session = Depends(get_db), request: UserBase = None):
    new_user = DbUser(
        username=request.username,
        email=request.username,
        password=Hash.hash(request.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_username(username: str, db: Session = Depends(get_db)):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            details=f'User with username {username} not found')
    return user
