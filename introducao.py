from fastapi import FastAPI

app = FastAPI(title="Loja", version=" 1.0")


@app.get("/produtos")
def listar_produtos():
    return ["caneta", "caderno"]


documento = app.openapi()
print(documento["openapi"])
print(list(documento["paths"]))
print(documento["info"]["title"], documento["info"]["version"])
