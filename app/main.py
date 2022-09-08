from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import post, user, auth, vote

app = FastAPI()

origins = ['*']

# global accessibility
app.add_middleware(
    CORSMiddleware,
    allow_origns=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

# sqlalchemy code
# models.Base.metadata.create_all(bind=engine)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# routing
# @app.get('/')
# def root():
#     return {'message': 'Hello World'}
