from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from config import oauth2
import schemas

from repositories import projects
from database import get_db  

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)

@router.get("/", response_model=List[schemas.Project], status_code=status.HTTP_200_OK)
def get_all_projects(db: Session = Depends(get_db)):
    return projects.get_all_projects(db)

@router.post("/", response_model=schemas.Project, status_code=status.HTTP_201_CREATED)
def create_project(request: schemas.Project, db: Session = Depends(get_db)):
    return projects.create_project(request, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(id: int, db: Session = Depends(get_db)):
    return projects.destroy_project(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_project(id: int, request: schemas.Project, db: Session = Depends(get_db)):
    return projects.update_project(id, request, db)

@router.get("/{id}", response_model=schemas.Project, status_code=status.HTTP_200_OK)
def read_project(id: int, db: Session = Depends(get_db)):
    return projects.show_project(id, db)
