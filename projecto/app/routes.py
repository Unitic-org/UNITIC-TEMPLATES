from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates_html")

# Fake database
templates_db = [
    {
        "id": 1,
        "name": "Barber Pro Landing",
        "description": "Landing page para barbearias",
        "price": 25,
        "preview_url": "/static/barber-preview.html"
    },
    {
        "id": 2,
        "name": "Pizza Express Landing",
        "description": "Landing page para pizzarias",
        "price": 25,
        "preview_url": "/static/pizza-preview.html"
    },
    {
        "id": 3,
        "name": "Clinic Vida+",
        "description": "Landing page para clínicas",
        "price": 30,
        "preview_url": "/static/clinic-preview.html"
    },
    {
        "id": 4,
        "name": "Power Gym Landing",
        "description": "Landing page para academias",
        "price": 25,
        "preview_url": "/static/gym-preview.html"
    }
]

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "templates": templates_db
    })

@router.get("/template/{id}", response_class=HTMLResponse)
def template_detail(request: Request, id: int):
    template = next((t for t in templates_db if t["id"] == id), None)
    
    return templates.TemplateResponse("template_detail.html", {
        "request": request,
        "template": template
    })