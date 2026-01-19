from dotenv import load_dotenv
from pydantic_settings import BaseSettings

_ = load_dotenv()


class Config(BaseSettings):
    db_name: str = "test.db"
    db_path: str = "./tmp"

    @property
    def db_url(self):
        return f"sqlite:///{self.db_path}/{self.db_name}"


config = Config()
