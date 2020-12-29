from typing import Optional
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/troll-api")
def troll_mind():
    return {"troll": "Great! Aliens have taken over :troll"}


@app.get("/troll", response_class=HTMLResponse)
async def read_static(request: Request):
    return templates.TemplateResponse("item.html", {"request": request})
