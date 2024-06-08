import sqlite3
from conexion_base import get_db_connection

def agregar_imagen(link, descripcion, id_cabania = "NULL"):
    '''
    Agrega url de imagen a la base de datos, el parametro id_cabania es opcional. Devuelve True si la operación es exitosa.
    '''
    cambios = 0
    conn = get_db_connection()
    if conn is not None: 
        query = """Insert into Imagenes values
                (?, ?, ?)"""
        conn.execute(query,(link, id_cabania, descripcion))
        cambios = conn.total_changes
        conn.close()
    return cambios > 0

def eliminar_imagen(link):
    '''
    Elimina la url de imágen ingresada de la base de datos. Devuelve True si la operación es exitosa.
    '''
    cambios = 0
    conn = get_db_connection()
    if conn is not None:
        query = """Delete from Imagenes
                Where link = ?"""
        conn.execute(query, (link,))
        cambios = conn.total_changes
        conn.close()
    return cambios > 0

def obtener_imagenes(cabania_id = None):
    '''
    Obtiene una lista de las imágenes almacenadas en la base de datos -links-,
    si no se especifica la cabania_id se devuelven las fotos sin vinculación a la tabla “cabanias”. 
    
    El formato de devolución es de diccionario:
    {“descripcion”: link, “descripcion2”: link2, …..}
    '''
    lista_variables = []
    res = {}

    if cabania_id is None:
        condicion_consulta = "is Null"
    else:
        condicion_consulta = "= ?"
        lista_variables.append(cabania_id)

    conn = get_db_connection()

    if conn is not None:
        query = "SELECT descripcion, imagen_link FROM Imagenes WHERE cabania_id " + condicion_consulta
        imagenes = conn.execute(query, tuple(lista_variables)).fetchall()
        conn.close()

        for imagen in imagenes:
            res[imagen["descripcion"]] = imagen["imagen_link"]

    return res

