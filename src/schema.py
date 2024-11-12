# Schema é a minah View do MVC

from pydantic import BaseModel

class PokemonSchema(BaseModel):
    name: str
    type: str

    class Config:
        orm_mode = True