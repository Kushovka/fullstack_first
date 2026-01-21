from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.models.user import User
from app.schemas.user import UserRead, UserCreate

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[UserRead])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@router.post("/", response_model=UserRead)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    user = User(**data.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
