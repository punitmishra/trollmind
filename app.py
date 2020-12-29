from typing import Optional
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/troll")
def troll_mind():
    return {"troll": "Great! Aliens have taken over :troll"}


@app.get("/rs/{id}", response_class=HTMLResponse)
async def read_static(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})
