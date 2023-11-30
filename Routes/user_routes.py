from Models import User
from fastapi import HTTPException, status
from Environment.dependencies import dependency
from fastapi import APIRouter
from typing import List

router = APIRouter()


@router.post("/user/", status_code=status.HTTP_201_CREATED, response_model=User.UserBase)
async def create_user(user: User.UserBase, db: dependency):
    db_user = User.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.put("/user/{user_id}", status_code=status.HTTP_200_OK, response_model=User.UserBase)
async def update_user(user_id: int, user: User.UserBase, db: dependency):
    db_user = db.query(User.User).filter(User.User.id == user_id).first()

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    for var, value in vars(user).items():
        setattr(db_user, var, value) if value else None

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


# GET endpoint to retrieve all roles
@router.get("/user/", status_code=status.HTTP_200_OK, response_model=List[User.UserWithID])
async def read_all_users(db: dependency):
    users = db.query(User.User).all()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users


@router.get("/user/{user_id}", status_code=status.HTTP_200_OK, response_model=User.UserWithID)
async def read_user(user_id: int, db: dependency):
    user = db.query(User.User).filter(User.User.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/user/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: dependency):
    user = db.query(User.User).filter(User.User.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()

    return None  # Returning None with status_code 204 NO CONTENT
