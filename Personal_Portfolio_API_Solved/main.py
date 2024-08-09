from fastapi import FastAPI
from router import blog,contact_info,projects,user_auth
from database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the auth router
app.include_router(user_auth.router)
app.include_router(blog.router)
app.include_router(projects.router)
app.include_router(contact_info.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Personal portfolio hub"}