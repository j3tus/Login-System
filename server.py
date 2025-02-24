import uvicorn
from fastapi import Request, FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
templates = Jinja2Templates("frontend/templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Basic routes


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/auth/login")
async def login(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})


@app.get("auth/register")
async def index(request: Request):
    return templates.TemplateResponse("auth/register.html", {"request": request})
