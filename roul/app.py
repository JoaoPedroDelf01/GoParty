import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
    
)


# Lista vazia — será preenchida pelo seu programa quando vincular ao frontend
ESTABELECIMENTOS: list[str] = []


@app.post("/adicionar")
def adicionar(data: dict): 
    place = data["place"]
    """Adiciona um estabelecimento à seleção do usuário."""
    
    if place in ESTABELECIMENTOS:
        return{ "status": False,
            "erro": f"'{place}' já está na lista."}
        
    ESTABELECIMENTOS.append(place)
    return { "status": True,
        "mensagem": f"'{place}' adicionado com sucesso."}
    
@app.delete("/remover")
def remover(data: dict):
    """Remove um estabelecimento da seleção do usuário."""
    
    place = data["place"]
    
    if place not in ESTABELECIMENTOS:
        return {"status": False,
                "erro": f"{place} não encontrado"}
    
    ESTABELECIMENTOS.remove(place)
    return {"status": True,
        "mensagem": f"'{place}' removido com sucesso."}
    
@app.get("/lista")
def listar():
    """Comando de retorno para ver se realmente o backend está funcionando.\nSó exibi no console"""
    
    if not ESTABELECIMENTOS:
       return {"status": False,
               "mensagem": "ERROR!"
        }
    
    return {"status": True,
            "ESTABELECIMENTOS": ESTABELECIMENTOS
    } 



@app.get("/sortear")
def sortear():
    """Sorteia 1 vencedor entre os estabelecimentos adicionados."""
    
    if not ESTABELECIMENTOS:
        return {"status": False,
            "erro": "Adicione ao menos um estabelecimento antes de sortear."}

    vencedor = random.choice(ESTABELECIMENTOS)
    return { "status": True,
        "vencedor": vencedor}
