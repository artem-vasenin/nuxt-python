from fastapi import FastAPI

from .project.routes import router as projectRouter

app = FastAPI(
    title='Jira Projects',
    description='Jira analog',
    version='0.0.1',
)
app.include_router(projectRouter)
