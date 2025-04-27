from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Literatur und Kunst API Manager",
    description="Eine API zur Suche nach Büchern, Autoren, Kunstwerken und zur Erstellung von DALL-E Prompts basierend auf gefundenen Stilen.",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Willkommen zur Literatur-Kunst-API. Bitte rufe /docs für die API-Dokumentation auf."}

class QueryRequest(BaseModel):
    prompt: str

class DallePromptRequest(BaseModel):
    author: str = ""
    artwork: str = ""

@app.post("/intelligent-query")
def intelligent_query(request: QueryRequest):
    return {
        "gutenberg_books": [f"Beispielbuch von {request.prompt}"],
        "rijksmuseum_art": [f"Bildlink zu {request.prompt}"],
        "europeana_art": [f"Artefaktlink zu {request.prompt}"]
    }

@app.post("/generate-dalle-prompt")
def generate_dalle_prompt(request: DallePromptRequest):
    parts = []
    if request.author:
        parts.append(f"inspired by {request.author}")
    if request.artwork:
        parts.append(f"in the style of {request.artwork}")
    base_prompt = "A dramatic, detailed digital artwork " + " and ".join(parts)
    base_prompt += ", dark atmosphere, medieval feeling."
    return {"prompt": base_prompt}