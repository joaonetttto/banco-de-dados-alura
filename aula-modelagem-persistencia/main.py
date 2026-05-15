from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas 
from database import SessionLocal, engine
from typing import List
from sqlalchemy import joinedload

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.post("/estudantes/", response_model=schemas.Estudante)