from pydantic import BaseModel

class Template(BaseModel):
    id: int
    name: str
    description: str
    price: float
    preview_url: str