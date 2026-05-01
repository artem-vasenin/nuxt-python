from fastapi import FastAPI

from .project.routes import router as projectRouter

app = FastAPI()
app.include_router(projectRouter)
