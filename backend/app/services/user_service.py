from sqlalchemy.orm import Session
from app.models.user import User as UserModel
from app.schemas.user_schema import UserCreate


def user_list(db: Session):
    return db.query(UserModel).all()


def create_user(db: Session, data: UserCreate):
    user = UserModel(name=data.name, age=data.age)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
