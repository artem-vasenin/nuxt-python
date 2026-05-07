from fastapi import FastAPI

from app.core.middlewares import TimingMW
from .project.routes import router as projectRouter
from .task.routes import router as taskRouter
from .user.routes import router as userRouter
from app.core.settings import Settings


def create_app()->FastAPI:
    settings = Settings() # type: ignore[call-arg]
    new_app = FastAPI(
        title=settings.app.title,
        description=settings.app.description,
        version=settings.app.version,
        openapi_tags=[
            {'name': 'Projects', 'description': 'Проекты'},
            {'name': 'Tasks', 'description': 'Задачи'},
            {'name': 'Auth', 'description': 'Пользователи'},
        ]
    )
    new_app.state.settings = settings
    new_app.include_router(projectRouter)
    new_app.include_router(taskRouter)
    new_app.include_router(userRouter)

    new_app.add_middleware(TimingMW)
    return new_app

app = create_app()
