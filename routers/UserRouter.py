from fastapi import Depends, HTTPException,APIRouter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import User
from models import UserCreate, UserResponse
from database import get_db

router = APIRouter(
    prefix="/user",
    tags=["users"]
)

@router.get("/", response_model=list[UserResponse],operation_id="get_users")
async def read_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).order_by(User.user_id))
    users = result.scalars().all()
    return users

@router.post("/post", response_model=UserCreate,operation_id="post_user")
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    new_user = User(name=user.name,surname=user.surname,age=user.age)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

@router.put('/put/{id}', response_model=UserCreate,operation_id="put_user")
async def update_user(id: int, updated_user: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.user_id == id))
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.name = updated_user.name
    user.surname = updated_user.surname
    user.age = updated_user.age
    await db.commit()
    await db.refresh(user)
    return user

@router.delete('/delete/{id}',operation_id="delete")
async def delete_user(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.user_id == id))
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    await db.delete(user)
    await db.commit()

    return {"message": f"User with id {id} has been deleted successfully"}
