from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def get_users(db: Session):

    users_all = db.query(models.Users).all()
    users_all = [new_data.to_dict() for new_data in users_all] if users_all else users_all

    res = {
        'users_all': users_all,
    }
    return res

async def get_users_id(db: Session, id: int):

    users_one = db.query(models.Users).filter(models.Users.id == id).first() 
    users_one = users_one.to_dict() if users_one else users_one

    res = {
        'users_one': users_one,
    }
    return res

async def post_users(db: Session, raw_data: schemas.PostUsers):
    id:str = raw_data.id
    created_at:str = raw_data.created_at
    updated_at:str = raw_data.updated_at
    email:str = raw_data.email
    password_hash:str = raw_data.password_hash


    record_to_be_added = {'id': id, 'created_at': created_at, 'updated_at': updated_at, 'email': email, 'password_hash': password_hash}
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    users_inserted_record = new_users.to_dict()

    res = {
        'users_inserted_record': users_inserted_record,
    }
    return res

async def put_users_id(db: Session, raw_data: schemas.PutUsersId):
    id:str = raw_data.id
    created_at:str = raw_data.created_at
    updated_at:str = raw_data.updated_at
    email:str = raw_data.email
    password_hash:str = raw_data.password_hash


    users_edited_record = db.query(models.Users).filter(models.Users.id == id).first()
    for key, value in {'id': id, 'created_at': created_at, 'updated_at': updated_at, 'email': email, 'password_hash': password_hash}.items():
          setattr(users_edited_record, key, value)
    db.commit()
    db.refresh(users_edited_record)
    users_edited_record = users_edited_record.to_dict() 

    res = {
        'users_edited_record': users_edited_record,
    }
    return res

async def delete_users_id(db: Session, id: int):

    users_deleted = None
    record_to_delete = db.query(models.Users).filter(models.Users.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict() 

    res = {
        'users_deleted': users_deleted,
    }
    return res

async def post_login(db: Session, raw_data: schemas.PostLogin):
    email:str = raw_data.email
    password:str = raw_data.password


    exists = db.query(models.Users).filter(models.Users.email == email).first() 
    exists = exists.to_dict() if exists else exists


    # add random
    password_hash: str = exists['password_hash']


    

    try:
        def authenticate_user(password:str, password_hash:str):
            if exists:
                # User with the provided email exists
                # stored_password_hash = exists['password_hash']
                if password == password_hash:
                    return True
                else:
                    return False
            else:
                # No user found with the provided email
                return False
        
        # Example usage:
        result = authenticate_user(password, password_hash)
        if not result:
            raise Exception("password doesnt match")
        
        # print(result)
    except Exception as e:
        raise HTTPException(500, str(e))


    res = {
        'result': exists,
    }
    return res

async def post_parking_lot(db: Session, raw_data: schemas.PostParkingLot):
    name:str = raw_data.name
    location:str = raw_data.location
    capacity:int = raw_data.capacity
    id:int = raw_data.id
    created_at:str = raw_data.created_at
    updated_at:str = raw_data.updated_at
    user_id:int = raw_data.user_id


    
    from datetime import datetime

    try:
        current_time = datetime.now()
    except Exception as e:
        raise HTTPException(500, str(e))



    record_to_be_added = {'id': id, 'created_at': created_at, 'updated_at': updated_at, 'user_id': user_id, 'name': name, 'location': location, 'capacity': capacity}
    new_parking_lots = models.ParkingLots(**record_to_be_added)
    db.add(new_parking_lots)
    db.commit()
    db.refresh(new_parking_lots)
    result = new_parking_lots.to_dict()

    res = {
        'Returnas': id,
    }
    return res

async def get_parking(db: Session, id: int):

    field_value = db.query(models.ParkingLots).all()
    field_value = [new_data.to_dict() for new_data in field_value] if field_value else field_value

    res = {
        'ReturnAs': field_value,
    }
    return res

