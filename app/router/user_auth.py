from fastapi import FastAPI,Depends,APIRouter,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from repositories import user
import models
import database
from database import  Base,engine
import schemas
from config.hashing import Hash
from config import token

get_db = database.get_db
Base.metadata.create_all(bind=engine)
app = FastAPI()


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/signup",status_code=status.HTTP_201_CREATED)
def create_user(request:schemas.UserCreate,db: Session = Depends(get_db)):
    new_user = user.createUser(request,db)
    return {"message": "Account successfully created", "user": new_user}
    

@router.post("/login")
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")

    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}