from sqlalchemy.orm import Session
from sqlalchemy import func

from ..configurations.models import Item
from ..configurations.models import User
from ..configurations import schemas

#database commit operations -> takes session and object to add to database and refresh
def commit_to_database(db: Session, objectToAdd: any):
    db.add(objectToAdd)
    db.commit()
    db.refresh(objectToAdd)
    return

# database operations
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = User(email=user.email, hashed_password=fake_hashed_password)
    commit_to_database(db, db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = Item(**item.dump(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# get users along with the count of their items
def get_user_items(db: Session):
    return db.query(User.id, func.count(Item.id)).join(Item).group_by(User.id).all()

