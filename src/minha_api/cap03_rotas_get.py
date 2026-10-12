from fastapi import FastAPI
from fastapi.testclient import TestClient

from starlette.routing import Route

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Bem-vindo ao FastAPI"}


@app.get("/sobre")
def sobre():
    return {"message": "Está é a página sobre"}


@app.get("/usuarios")
def usuarios():
    return {"usuarios": ["Oliver", "Fred", "Hanna"]}


@app.get("/produtos", tags=["Produtos"], summary="Lista de Produtos")
def produtos():
    """Devolve todos os produtos disponíveis no catálogo"""
    return []


@app.get("/categorias")
def categorias():
    return {"categorias": ["Livros", "Jogos", "Músicas"]}
