import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
    
)


# Lista vazia — será preenchida pelo seu programa quando vincular ao frontend
BARES: list[str] = []


@app.post("/adicionar")
def adicionar(data: dict):
    bar = data["bar"]
    """Adiciona um bar à seleção do usuário."""
    if bar in BARES:
        return{ "status": False,
            "erro": f"'{bar}' já está na lista."}
    BARES.append(bar)
    return { "status": True,
        "mensagem": f"'{bar}' adicionado com sucesso."}
    
@app.get("/lista")
def listar():
    if not BARES:
       return {"status": False,
               "mensagem": "ERROR!"
        }
    
    return {"status": True,
            "bares": BARES
    }

@app.delete("/remover")
def remover(bar: dict):
    """Remove um bar da seleção do usuário."""
    if bar not in BARES:
        return {"status": False,
                "erro": f"{bar} não encontrado"}
    
    BARES.remove(bar)
    return {"status": True,
        "mensagem": f"'{bar}' removido com sucesso."}


@app.post("/sortear")
def sortear():
    """Sorteia 1 vencedor entre os bares adicionados."""
    if not BARES:
        return {"status": False,
            "erro": "Adicione ao menos um bar antes de sortear."}

    vencedor = random.choice(BARES)
    return { "status": True,
        "vencedor": vencedor}
