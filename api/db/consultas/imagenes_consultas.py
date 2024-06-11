from db.consultas.conexion_base import get_db_connection
import sqlite3
import sys
import os

# Añadir el directorio del paquete a sys.path de manera dinámica
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))


def agregar_imagen(link, descripcion, id_cabania=None):
    '''
    Agrega url de imagen a la base de datos, el parametro id_cabania es opcional. Devuelve True si la operación es exitosa.
    '''
    cambios = 0
    conn = get_db_connection()
    if conn is not None:
        query = """Insert into Imagenes values
                (?, ?, ?)"""
        conn.execute(query, (link, id_cabania, descripcion))
        conn.commit()
        cambios = conn.total_changes
        conn.close()
    return cambios > 0


def eliminar_imagen(link = None, cabania_id = None):
    '''
    Elimina la url de imágen ingresada de la base de datos. Devuelve True si la operación es exitosa.
    Si se ingresa un Cabania_Id elimina por el id de cabaña todo el grupo de links asociado a la misma.

    Pre-Condición: No se puede eliminar por el link y cabania_id al mismo tiempo
    '''
    if cabania_id is None and link is None:
        return False
    
    cambios = 0
    parametros = []
    conn = get_db_connection()
    if conn is not None:    
        if cabania_id is not None:
            query = """Delete from Imagenes
                       where cabania_id = ?"""
            parametros.append(cabania_id)

        if link is not None :
            query = """Delete from Imagenes
                       where link = ?"""
            parametros.append(link)
            
        conn.execute(query, tuple(parametros))
        conn.commit()
        cambios = conn.total_changes
        conn.close()
    return cambios > 0


def obtener_imagenes(cabania_id=None):
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

        for descripcion, link in imagenes:
            res[descripcion] = link

    return res

