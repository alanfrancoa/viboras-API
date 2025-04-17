from flask import Flask, request
from utils.cargar_datos import cargar_viboras

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

