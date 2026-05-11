from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models 
import schemas
from database import SessionLocal, engine

#cria  as tabelas no postgreSQL(caso não existam)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.post('/estudantes/', response_model=schemas.EstudantesResponse)

def create_student(
    student: schemas.EstudantesCreate, 
        db: Session = Depends(get_db)): 
        db_student = models.Estudantes(**student.model_dump())
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student
    
@app.get('/estudantes/', response_model=list[schemas.EstudantesResponse])
def read_students(db: Session = Depends(get_db())):
    students = db.query(models.Estudantes).all()
    return students
