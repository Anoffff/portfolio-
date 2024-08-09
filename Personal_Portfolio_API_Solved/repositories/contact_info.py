from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import models
import schemas


def create_contactinfo(request: schemas.ContactInfo, db: Session):
    new_contactinfo = models.ContactInfo(name=request.name, email=request.email, phone=request.phone, user_id=request.user_id)
    db.add(new_contactinfo)
    db.commit()
    db.refresh(new_contactinfo)
    return new_contactinfo

def destroy_contactinfo(id: int, db: Session):
    contactinfo = db.query(models.ContactInfo).filter(models.ContactInfo.id == id)

    if not contactinfo.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Contact Info with id {id} not found")

    contactinfo.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update_contactinfo(id: int, request: schemas.ContactInfo, db: Session):
    contactinfo = db.query(models.ContactInfo).filter(models.ContactInfo.id == id)

    if not contactinfo.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Contact Info with id {id} not found")

    contactinfo.update(request.dict())
    db.commit()
    return 'updated'

def show_contactinfo(id: int, db: Session):
    contactinfo = db.query(models.ContactInfo).filter(models.ContactInfo.id == id).first()
    if not contactinfo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Contact Info with id {id} is not available")
    return contactinfo
