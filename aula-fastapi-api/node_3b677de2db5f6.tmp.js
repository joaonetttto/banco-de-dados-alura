from pydantic import BaseModel

class Estudantesbase(BaseModel):
    nome: str
    idade: int
    
class EstudantesCreate(Estudantesbase):
    pass

class EstudantesResponse(Estudantesbase):
    id: int
    class Config:
        from_attributes = True
        
class MatriculasBase(BaseModel):
    estudante_id: int
    nome_disciplina: str
    
class MatriculasCreate(MatriculasBase):
    pass

class MatriculasResponse(MatriculasBase):
    id: int
    class Config:
        from_attributes = True