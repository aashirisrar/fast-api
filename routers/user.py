from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import schemas
from ..models import User
from ..configurations.database import get_database_session
from ..services.database_operations import get_all, get_by_id,create_user

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.post("/createuser/", response_model=schemas.User)
def create_user_(user: schemas.UserCreate, db: Session = Depends(get_database_session)):
    return create_user(db=db, user=user)


@router.get("/allusers/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, database: Session = Depends(get_database_session)):
    return get_all(database, User, skip, limit)
    

@router.get("/getuser/{user_id}/", response_model=schemas.User)
def read_user(user_id: int, database: Session = Depends(get_database_session)):
    user_in_database = get_by_id(database, User,user_id)
    if user_in_database is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_in_database