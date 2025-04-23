from flask import Flask, request
from utils.cargar_datos import cargar_viboras
from filters.filtros import *

app = Flask(__name__)

@app.route('/')
def main():
    return{
        "Message": "Bienvenide al API de viboras",
        "Autor": "Alan F. Alvarez",
        "Description": "App desarrollada con fines educativos para TP de Taller integral de Programacion"
        }

#[GET] - Obtener todas las serpientes
@app.route('/vibora/all')
def get_Viboras():
    #Traemos todas las viboras
    data = cargar_viboras()
    return data

#[GET] - Obtener la vibora por ID
@app.route('/vibora/id/<int:id_vibora>')
def get_vibora_by_id(id_vibora):
    data = cargar_viboras()
    
    if "serpientes" in data:
        res = filtrar_por_id(data["serpientes"], id_vibora)  # Pasamos solo la lista
    else:
        res = None
    
    if res:
        return res, 200  # Usar 200 (OK) 
    return {'message': 'Vibora no encontrada'}, 404