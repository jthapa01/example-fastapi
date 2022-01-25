from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)
app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)  # grab router obj from user file
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")  # decorator
async def root():
    return {"message": "Hello World!"}


# pydantic model, defining schema for post or update

# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
#             {"title": "favorite food", "content": "pizza", "id": 2}]


# def find_post(id):
#     for p in my_posts:
#         if p['id'] == id:
#             return p

# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i
