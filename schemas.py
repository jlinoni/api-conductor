from pydantic import BaseModel
class Conductor(BaseModel):
    nombres: str
    edad: int
    direccion: str
    licencia: str