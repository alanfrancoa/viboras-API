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

#funcion para obtener las viboras por ID
def filtrar_por_nombre(data, nombre):

    #guardamos nombre en minusculas.
    min_nombre = nombre.lower()

    #recorremos JSON
    for vibora in data:

        #obtenemos el nombre de la vibora actual
        current_name = vibora['nombre_comun'].lower()

        if min_nombre == current_name:
            return vibora
    
    return None