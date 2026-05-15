from typing import List, Optional
from pydantic import BaseModel

class Estudante(BaseModel):
    id: int
    nome: str
    perfil: Optional[str] = None
    
    class Config:
        from_attributes = True
        
class Estudante_create(BaseModel):
    nome: str
    email : str
    perfil: PerfilCreate
    
class PerfilCreate(BaseModel):
    id: int
    idade: int
    endereco: str
    
    class Config:
        from_atributes = True
        
        
class PerfilCreate(BaseModel):
    idade: int
    endereco: str