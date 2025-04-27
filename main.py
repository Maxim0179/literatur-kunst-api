from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Literatur-Kunst-API is alive!"}

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