from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict



class Product(BaseModel):
    product_id: int
    product_name: str
    category:str
    price: float
    stock_quantity: int

class CarInput(BaseModel):
    buying: str
    maint: str
    doors: str
    persons: str
    lug_boot: str
    safety: str


class Settings(BaseSettings):
    db_host: str
    db_user: str
    db_password: str
    db_name: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
    # class Config:
    #     env_file = ".env"


settings = Settings()

