from mirascope.groq import GroqExtractor, GroqCallParams

from fastapi import FastAPI

from pydantic import BaseModel, Field
from typing import Type, List

from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class Publicaiton(BaseModel):
    accroch: str = Field(..., title="Accroche de la publication")
    contenu:str= Field(..., title="Contenu de la publication")
    hashtags: List[str] = Field(default_factory=list , description="Liste des mots-cle de la publication")