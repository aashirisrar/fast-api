from sqlalchemy.orm import Session

from typing import Any, List

from .. import schemas

def commit_to_database(database: Session, object_to_add: Any):
    database.add(object_to_add)
    database.commit()
    database.refresh(object_to_add)
    return object_to_add

def get_by_id(database: Session, model: Any, id: int) -> schemas.Item | schemas.User:
    return database.query(model).filter(model.id == id).first()

def get_all(database: Session, model: Any, skip: int = 0, limit: int = 100) -> List[schemas.User] | List[schemas.Item]:
    return database.query(model).offset(skip).limit(limit).all()

def create_instance(database: Session, model: Any, object: Any) -> schemas.UserCreate | schemas.ItemCreate:
    database_obj = model(**object.dict())
    return commit_to_database(database, database_obj)