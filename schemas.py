from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Users(BaseModel):
    id: int
    created_at: datetime.time
    updated_at: datetime.time
    email: str
    password_hash: str


class ReadUsers(BaseModel):
    id: int
    created_at: datetime.time
    updated_at: datetime.time
    email: str
    password_hash: str
    class Config:
        from_attributes = True


class ParkingLots(BaseModel):
    id: int
    created_at: str
    updated_at: str
    user_id: int
    name: str
    location: str
    capacity: int


class ReadParkingLots(BaseModel):
    id: int
    created_at: str
    updated_at: str
    user_id: int
    name: str
    location: str
    capacity: int
    class Config:
        from_attributes = True


class ParkingSlots(BaseModel):
    id: int
    created_at: datetime.time
    parking_lot_id: int
    slot_type: str
    hourly_rate: float
    is_occupied: bool


class ReadParkingSlots(BaseModel):
    id: int
    created_at: datetime.time
    parking_lot_id: int
    slot_type: str
    hourly_rate: float
    is_occupied: bool
    class Config:
        from_attributes = True


class Vehicles(BaseModel):
    id: int
    created_at: datetime.time
    updated_at: datetime.time
    parking_lot_id: int
    registration_id: str
    owner_name: str
    phone_number: str
    model_type: str
    color: str


class ReadVehicles(BaseModel):
    id: int
    created_at: datetime.time
    updated_at: datetime.time
    parking_lot_id: int
    registration_id: str
    owner_name: str
    phone_number: str
    model_type: str
    color: str
    class Config:
        from_attributes = True


class ClockInOut(BaseModel):
    id: int
    created_at: datetime.time
    vehicle_id: int
    parking_slot_id: int
    clock_in_time: datetime.time
    clock_out_time: datetime.time
    total_cost: float


class ReadClockInOut(BaseModel):
    id: int
    created_at: datetime.time
    vehicle_id: int
    parking_slot_id: int
    clock_in_time: datetime.time
    clock_out_time: datetime.time
    total_cost: float
    class Config:
        from_attributes = True




class PostUsers(BaseModel):
    id: str
    created_at: str
    updated_at: str
    email: str
    password_hash: str

    class Config:
        from_attributes = True



class PutUsersId(BaseModel):
    id: str
    created_at: str
    updated_at: str
    email: str
    password_hash: str

    class Config:
        from_attributes = True



class PostLogin(BaseModel):
    email: str
    password: str

    class Config:
        from_attributes = True



class PostParkingLot(BaseModel):
    name: str
    location: str
    capacity: int
    id: int
    created_at: str
    updated_at: str
    user_id: int

    class Config:
        from_attributes = True

