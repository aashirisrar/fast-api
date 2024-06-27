from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import schemas
from ..models import Item
from ..configurations.database import get_database_session
from ..services.database_operations import get_all, get_by_id,create_user, create_item

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

@router.get("/allitems/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, database: Session = Depends(get_database_session)):
    return get_all(database, Item ,skip=skip, limit=limit)


@router.get("/getitem/{item_id}/", response_model=schemas.Item)
def read_user(item_id: int, database: Session = Depends(get_database_session)):
    item_in_database = get_by_id(database, Item,item_id)
    if item_in_database is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item_in_database

@router.post("/createitem/")
def create_item_(item: schemas.Item, db: Session = Depends(get_database_session)):
    return create_item(db=db, item=item)
    