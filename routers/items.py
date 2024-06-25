from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..dependencies import schemas

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

@router.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

#get users and their items
@router.get("/usersanditems", tags= ["Users and Items"])
def get_all_items(db: Session = Depends(get_db)):
    users_items = crud.get_user_items(db)
    return users_items;
