from Models import Search
from fastapi import HTTPException, status
from Environment.dependencies import dependency
from fastapi import APIRouter
from typing import List

router = APIRouter()


@router.post("/search/", status_code=status.HTTP_201_CREATED, response_model=Search.SearchBase)
async def create_search(search: Search.SearchBase, db: dependency):
    db_search = Search.Search(**search.dict())
    db.add(db_search)
    db.commit()
    db.refresh(db_search)
    return db_search

