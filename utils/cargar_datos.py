import json

def cargar_viboras():
    with open('data/viboras.json', 'r', encoding='utf-8') as f:
        return json.load(f)