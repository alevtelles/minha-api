from fastapi.testclient import TestClient

from minha_api.cap03_rotas_get import app

cliente = TestClient(app)


def test_home():
    resposta = cliente.get("/")
    assert resposta.status_code == 200
    assert resposta.json() == {"message": "Bem-vindo ao FastAPI"}


def test_sobre():
    resposta = cliente.get("/sobre")
    assert resposta.status_code == 200
    assert resposta.json() == {"message": "Está é a página sobre"}


def test_usuarios():
    resposta = cliente.get("/usuarios")
    assert resposta.status_code == 200
    assert resposta.json() == {"usuarios": ["Oliver", "Fred", "Hanna"]}


def test_produtos():
    resposta = cliente.get("/produtos")
    assert resposta.status_code == 200
    assert resposta.json() == []


def test_categorias():
    resposta = cliente.get("/categorias")
    assert resposta.status_code == 200
    assert resposta.json() == {"categorias": ["Livros", "Jogos", "Músicas"]}
