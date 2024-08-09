from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from repositories import contact_info
import schemas
from database import get_db  

router = APIRouter(
    prefix="/contactinfo",
    tags=["ContactInfo"]
)

@router.post("/", response_model=schemas.ContactInfo, status_code=status.HTTP_201_CREATED)
def create_contactinfo(request: schemas.ContactInfo, db: Session = Depends(get_db)):
    return contact_info.create_contactinfo(request, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_contactinfo(id: int, db: Session = Depends(get_db)):
    return contact_info.destroy_contactinfo(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_contactinfo(id: int, request: schemas.ContactInfo, db: Session = Depends(get_db)):
    return contact_info.update_contactinfo(id, request, db)

@router.get("/{id}", response_model=schemas.ContactInfo, status_code=status.HTTP_200_OK)
def read_contactinfo(id: int, db: Session = Depends(get_db)):
    return contact_info.show_contactinfo(id, db)
