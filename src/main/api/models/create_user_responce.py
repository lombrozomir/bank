from typing import Optional
from src.main.api.models.base_model import BaseModel

class CreateUserResponse(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    password: Optional[str] = None
    role: Optional[str] = None
    error: Optional[str] = None
