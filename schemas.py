from pydantic import BaseModel
class Conductor(BaseModel):
    nombres: str
    edad: int
    direccion: str
    licencia: str

class Vehiculo(BaseModel):
    conductor_id: int
    marca: str
    modelo: str
    ano: int
    placa: str