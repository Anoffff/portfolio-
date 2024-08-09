from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import models
import schemas

def get_all_projects(db: Session):
    projects = db.query(models.Project).all()
    return projects

def create_project(request: schemas.Project, db: Session):
    new_project = models.Project(title=request.title, description=request.description, user_id=request.user_id)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

def destroy_project(id: int, db: Session):
    project = db.query(models.Project).filter(models.Project.id == id)

    if not project.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Project with id {id} not found")

    project.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update_project(id: int, request: schemas.Project, db: Session):
    project = db.query(models.Project).filter(models.Project.id == id)

    if not project.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Project with id {id} not found")

    project.update(request.dict())
    db.commit()
    return 'updated'

def show_project(id: int, db: Session):
    project = db.query(models.Project).filter(models.Project.id == id).first()
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Project with id {id} is not available")
    return project
