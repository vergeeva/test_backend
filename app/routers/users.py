from fastapi import APIRouter, Depends, status, Request
from ..database import get_db
from sqlalchemy.orm import Session
from .. import Models, schemas
from pydantic import EmailStr

router = APIRouter()


@router.get('/all_users', response_model=schemas.ListUserResponse)
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(Models.User).all()
    return {'users': users}


@router.post('/user_clicked', status_code=status.HTTP_201_CREATED)
def create_or_update_user(payload: schemas.UserBaseSchema, request: Request, db: Session = Depends(get_db)):
    # Проверим, есть ли такой пользователь в бд
    user_query = db.query(Models.User).filter(Models.User.email == EmailStr(payload.email.lower()))
    user = user_query.first()
    if not user:
        payload.click_count = 1
        new_user = Models.User(**payload.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    else:
        user.click_count += 1
        user_query.update(payload.dict(exclude_unset=True),synchronize_session=False)
        db.commit()
        return user



