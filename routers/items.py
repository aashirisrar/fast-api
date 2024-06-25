from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..dependencies import schemas
from ..dependencies.database import get_items, get_user_items

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

@router.get("/allitems/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = get_items(db, skip=skip, limit=limit)
    return items

#get users and their items
@router.get("/usersanditems/", tags= ["Users and Items"])
def get_all_items(db: Session = Depends(get_db)):
    users_items = get_user_items(db)
    return users_items;
