from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db import get_db
from app.schemas.user_schema import User, UserCreate
from app.services.user_service import create_user, user_list

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=List[User])
def list_users_endpoint(db: Session = Depends(get_db)):
    return user_list(db)


@router.post("/", response_model=User)
def create_user_enpoint(data: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, data)

