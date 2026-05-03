from fastapi import FastAPI

from .project.routes import router as projectRouter
from .task.routes import router as taskRouter
from app.core.settings import Settings


def create_app()->FastAPI:
    settings = Settings() # type: ignore[call-arg]
    new_app = FastAPI(
        title=settings.app.title,
        description=settings.app.description,
        version=settings.app.version,
    )
    new_app.state.settings = settings
    new_app.include_router(projectRouter)
    new_app.include_router(taskRouter)
    return new_app

app = create_app()
