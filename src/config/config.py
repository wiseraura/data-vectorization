from pydantic_settings import BaseSettings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

class Settings(BaseSettings):
    project_name: str
    debug: bool
    mongodb_uri: str
    mongodb_user: str
    mongodb_password: str

    gcp_api_key: str
    aws_access_key_id: str
    azure_api_key: str

    class Config:
        env_file = ".env"

async def init_db():
    client = AsyncIOMotorClient(Settings.mongodb_uri)
    await init_beanie(database=client.get_default_database(), document_models=model.__all__)