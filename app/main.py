from fastapi import FastAPI

from .posts.routes import router as postsRouter

app = FastAPI()
app.include_router(postsRouter)
