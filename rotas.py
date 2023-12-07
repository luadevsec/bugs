from fastapi import APIRouter, status, Depends, Request
from fastapi.responses import HTMLResponse
from view import home


rotas = APIRouter()

@rotas.get('/', response)
def home(request: Request):
    return home(request)