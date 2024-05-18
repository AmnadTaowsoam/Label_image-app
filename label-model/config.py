from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # Pre-label model configuration
    pre_label_model_name: str = Field(default='yolov5', env='PRE_LABEL_MODEL_NAME')
    pre_label_model_path: str = Field(default='path/to/pretrained/model', env='PRE_LABEL_MODEL_PATH')

    # Re-label model configuration
    re_label_model_name: str = Field(default='yolov5', env='RE_LABEL_MODEL_NAME')
    re_label_model_path: str = Field(default='path/to/retrained/model', env='RE_LABEL_MODEL_PATH')

    # API configuration
    api_host: str = Field(default='0.0.0.0', env='API_HOST')
    pre_label_api_port: int = Field(default=5000, env='PRE_LABEL_API_PORT')
    re_label_api_port: int = Field(default=5001, env='RE_LABEL_API_PORT')

    # Database configuration
    db_name: str = Field(default='labelstudio', env='DB_NAME')
    db_username: str = Field(default='postgres', env='DB_USERNAME')
    db_password: str = Field(default='password', env='DB_PASSWORD')
    db_host: str = Field(default='image-storage', env='DB_HOST')
    db_port: int = Field(default=5432, env='DB_PORT')

    class Config:
        env_file = '../.env'

settings = Settings()
