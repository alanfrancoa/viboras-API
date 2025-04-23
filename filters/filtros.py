#Funcion para obtener las viboras por ID
def filtrar_por_id(data, id):
    
    #asignamos el valor del ID y lo convertimos a String para compraracion.
    auto_id_param = id

    #recorro el JSON
    for vibora in data:

        #Obtenemos el id de la vibora actual
        current_id = vibora['id']

        #validamos si coincide con el ID buscado
        if current_id == auto_id_param:
            return vibora
        
    #Si el bucle finaliza y no hay coincidencias devolvemos NONE
    return None

