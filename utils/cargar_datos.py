import json

def cargar_viboras():
    with open('./data/viboras.json', 'r', encoding='utf-8') as f:  # <- Agrega encoding='utf-8'
        return json.load(f)