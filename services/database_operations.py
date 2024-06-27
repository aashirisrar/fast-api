from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from typing import Any, List

from .. import schemas
from .. import models

def commit_to_database(database: Session, object_to_add: Any):
    database.add(object_to_add)
    database.commit()
    database.refresh(object_to_add)
    return object_to_add

def get_by_id(database: Session, model: Any, id: int) -> schemas.Item | schemas.User:
    table_name = model.__tablename__
    query = text(f"SELECT * FROM {table_name} WHERE id={id} LIMIT 1");
    result = database.execute(query)
    return result.first()


def get_all(database: Session, model: Any, skip: int = 0, limit: int = 100) -> List[Any]:
    table_name = model.__tablename__
    query = text(f"SELECT * FROM {table_name} LIMIT {limit} OFFSET {skip}")
    result = database.execute(query)
    return result.fetchall()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_item(db: Session, item: schemas.Item):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item