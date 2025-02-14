from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    try:
        return await service.get_users(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/id')
async def get_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(raw_data: schemas.PostUsers, db: Session = Depends(get_db)):
    try:
        return await service.post_users(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/id/')
async def put_users_id(raw_data: schemas.PutUsersId, db: Session = Depends(get_db)):
    try:
        return await service.put_users_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id')
async def delete_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/login')
async def post_login(raw_data: schemas.PostLogin, db: Session = Depends(get_db)):
    try:
        return await service.post_login(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/parking/lot')
async def post_parking_lot(raw_data: schemas.PostParkingLot, db: Session = Depends(get_db)):
    try:
        return await service.post_parking_lot(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/parking')
async def get_parking(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_parking(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

