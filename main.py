from mirascope.groq import GroqExtractor, GroqCallParams

from fastapi import FastAPI

from pydantic import BaseModel, Field
from typing import Type, List

from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class Publication(BaseModel):
    accroch: str = Field(..., title="Accroche de la publication")
    contenu:str= Field(..., title="Contenu de la publication")
    hashtags: List[str] = Field(default_factory=list , description="Liste des mots-cle de la publication")

class PublicationCreator(GroqExtractor[Publication]):
    extract_schema: Type[Publication] = Publication

    sujet: str
    ton: str

    prompt_template = """
        Tu es un créateur de contenu très renommé sur LinkedIn.
    
        Tu dois créer un post LinkedIn sur le sujet fourni par l'utilisateur, en prenant soin d'adopter le ton demandé. 

        Le post doit être accrocheur, informatif et exhaustif. 

        Tu dois fournir une accroche qui doit être percutante et donner envie à l'utilisateur de lire la suite.

        Tu dois également fournir 3 ou 4 hashtags qui aideront pour le référencement de la publication.

        SUJET : {sujet}

        TON : {ton}
    """
    
    call_params = GroqCallParams(model="llama3-70b-8192",temperature=1)
    
@app.post("/create_publication")
def create_post(publication_creator: PublicationCreator) -> Publication:
    """Génère une publication LinkedIn"""
    return publication_creator.extract()