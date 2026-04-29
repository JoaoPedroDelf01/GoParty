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


@app.post("/append")
def adicionar(data: dict): 
    place = data["place"]
    """Adiciona um estabelecimento à seleção do usuário."""
    
    if place in ESTABELECIMENTOS:
        return{ "status": False,
            "erro": f"'{place}' já está na lista."}

    if not place or not place.strip():
        return{"status": False,
        "erro": f"'{place}' Não é um valor válido",
        "list": list_etc()}     
         
    ESTABELECIMENTOS.append(place)
    return { "status": True,
    "answer": f"'{place}' adicionado com sucesso.",
    "list": list_etc()}
    


@app.delete("/remove")
def remover(data: dict):
    """Remove um estabelecimento da seleção do usuário."""
    
    place = data["place"]
    
    if place not in ESTABELECIMENTOS:
        return {"status": False,
                "erro": f"{place} não encontrado"}
    
    ESTABELECIMENTOS.remove(place)
    return {"status": True,
        "answer": f"'{place}' removido com sucesso."}
     

def list_etc():
    """Retorna a quantidade de estabelecimentos"""
    
    if ESTABELECIMENTOS:
        return{"status": True,
            "answer": len(ESTABELECIMENTOS),
    } 
    return{"status": False,
           "erro": "ERROR!!"
    }

@app.get("/draw")
def draw_etc():
    """Sorteia 1 vencedor entre os estabelecimentos adicionados."""
    
    if not ESTABELECIMENTOS:
        return {"status": False,
            "erro": "Adicione ao menos um estabelecimento antes de sortear."}

    vencedor = random.choice(ESTABELECIMENTOS)
    return { "status": True,
        "answer": f"Sorteado: {vencedor}"}
