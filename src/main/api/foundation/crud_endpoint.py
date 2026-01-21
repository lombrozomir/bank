from dataclasses import dataclass
from enum import Enum
from typing import Type
from src.main.api.models.base_model import BaseModel

@dataclass(frozen=True)
class CrudEndpointData:
    url: str
    response_model: Type[BaseModel] = BaseModel

class CrudEndpoint(Enum):
    CREATE = CrudEndpointData('', BaseModel)
    DELETE = CrudEndpointData('', BaseModel)
