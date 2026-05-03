from typing import Annotated
from fastapi import Depends, Request
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class BDSettings(BaseModel):
    url: str

class AuthSettings(BaseModel):
    jwt: str

class AppSettings(BaseModel):
    title: str = 'Jira'
    description: str = 'Jira analog'
    version: str = '0.0.1'
    debug: bool = False

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')
    db_url: str = Field(validation_alias='DATABASE_URL')
    jwt_token: str

    @property
    def db(self)->BDSettings:
        return BDSettings(url=self.db_url)

    @property
    def app(self)->AppSettings:
        return AppSettings()

    @property
    def auth(self)->AuthSettings:
        return AuthSettings(jwt=self.jwt_token)

def get_settings(req: Request)->Settings:
    return req.app.state.settings

SettingsDeps = Annotated[
    Settings,
    Depends(get_settings)
]
