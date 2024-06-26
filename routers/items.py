from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..configurations.database import get_db
from ..configurations import schemas
from ..services.database_operations import get_items, get_user_items

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
