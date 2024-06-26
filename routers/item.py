from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import schemas
from ..models import Item
from ..configurations.database import get_database_session
from ..services.database_operations import get_all

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

@router.get("/allitems/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, database: Session = Depends(get_database_session)):
    return get_all(database, Item ,skip=skip, limit=limit)
