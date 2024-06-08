import sqlite3
from datetime import datetime
from conexion_base import get_db_connection
from imagenes_consultas import obtener_imagenes


def obtener_cabanias():
    '''
    Devuelve los datos de todas las cabañas en formato de diccionario de diccionario.
    Salida:
    {“cabaña_id1”: {“nombre“: str,
                    “capacidad_max“: int,
                    “imagenes”: { imagenes_cabania(cabaña) },
                    “descripcion“: str,
                    “precio_por_noche“: float},
    “cabaña_id2“: { … }, … }
    '''
    res = {}
    conn = get_db_connection()
    if conn is not None:
        cabanias = conn.execute("SELECT * FROM Cabanias").fetchall()
        conn.close()
        for cabania in cabanias:
            res[cabania["cabania_id"]] = {
                "nombre": cabania["nombre"],
                "cap_max": cabania["cap_max"],
                "imagenes": obtener_imagenes(cabania["cabania_id"]),
                "descripcion": cabania["descripcion"],
                "precio_noche": cabania["precio_noche"]}
    return res
print(obtener_cabanias())

def consultar_disponibilidad(cabania_id, fecha_ent, fecha_sal):
    '''
    Devuelve True si la cabaña elegida está libre para reservar en ese rango de fechas, caso contrario devuelve False.

    Pre-condiciones:
    fecha_ingreso y fecha_egreso deben tener el siguiente formato: “YYYY-MM-DD“.
    fecha_ingreso debe ser una fecha posterior a la fecha actual y debe ser anterior a fecha_egreso.
    '''
    conn = get_db_connection()
    if conn is not None:
        query = f"""
        SELECT COUNT(*) FROM Reservas
        WHERE (
            (cabania_id = ?) AND
            (? <= fecha_sal AND ? >= fecha_ent)
            )
        """
        res = conn.execute(query, (cabania_id, fecha_ent, fecha_sal)).fetchone()
        conn.close()
        return res[0] == 0


def calendario_reservas(cabania_id):
    '''
    Función auxiliar para usar en el diseño del calendario. 
    Devuelve una lista de diccionarios con el rango de fechas de cada reserva para la cabaña elegida. 
    
    Salida:
    [{'fecha_ent': '2023-03-01', 'fecha_sal': '2023-03-20'}, {'fecha_ent': '2023-06-01', 'fecha_sal': '2023-07-22'}, … ]
    '''
    conn = get_db_connection()
    reservas = []

    if conn is not None:
        query = f"""
        SELECT fecha_ent, fecha_sal FROM Reservas
        WHERE cabania_id = '?'
        """
        res = conn.execute(query, (cabania_id,)).fetchall()
        conn.close()
        for row in res:
            reserva = {
                "fecha_ent": row["fecha_ent"],
                "fecha_sal": row["fecha_sal"]
            }
            reservas.append(reserva)

    return reservas


def agregar_cabania(cabania_id, nombre, descripcion, cap_max, precio_noche):
    '''
    Agrega una cabaña a la base de datos. 
    Si la operación se realiza exitosamente devuelve True, sino devuelve False.

    Pre-condiciones: El id de la cabania esta formado por 'CAB_XXX' donde XXX son las iniciales de la cabaña
    '''
    changes = 0
    conn = get_db_connection()
    if conn is not None:
        try:
            conn.execute("Insert into Cabanias values (?,?,?,?,?)", (cabania_id, nombre, descripcion, cap_max, precio_noche))
            conn.commit()
            changes = conn.total_changes
        except sqlite3.Error as e:
            print("Error al modificar la cabaña:", e)
            conn.rollback()
        conn.close()

    return changes > 0

def eliminar_cabania(cabania_id):
    '''
    Elimina la cabaña según el cabania_id ingresado (de la base de datos).
    Si la operación se realiza exitosamente devuelve True, sino devuelve False.
    '''
    changes = 0
    conn = get_db_connection()
    if conn is not None:
        try:
            conn.execute("Delete from Cabanias where cabania_id = ?", (cabania_id,))
            conn.commit()
            changes = conn.total_changes
        except sqlite3.Error as e:
            print("Error al elminar la cabaña:", e)
            conn.rollback()
        conn.close()     
    return changes > 0

def modificar_cabania(cabania_id, nuevo_nombre = None, nueva_descripcion = None, nueva_cap_max = None, nuevo_precio_noche = None):
    '''
    Edita la cabaña según el cabania_id ingresado (de la base de datos).
    Si la operación se realiza correctamente devuelve True, sino False. 
    Los parametros ‘nuevo_elemento’ son opcionales.
    '''
    changes = 0
    conn = get_db_connection() 
    
    if conn is not None:
        query = "UPDATE Cabanias SET "
        valores = []
        condiciones = []

        if nuevo_nombre is not None:
            condiciones.append("nombre = ?")
            valores.append(nuevo_nombre)

        if nueva_descripcion is not None:
            condiciones.append("descripcion = ?")
            valores.append(nueva_descripcion)

        if nueva_cap_max is not None:
            condiciones.append("cap_max = ?")
            valores.append(nueva_cap_max)

        if nuevo_precio_noche is not None:
            condiciones.append("precio_noche = ?")
            valores.append(nuevo_precio_noche)

        condiciones_sql = ", ".join(condiciones)

        valores.append(cabania_id)
        condiciones_sql += " WHERE cabania_id = ?" #Agrega la condicion 

        #Consulta final
        query += condiciones_sql

        try:
            conn.execute(query, tuple(valores))
            conn.commit()
            changes = conn.total_changes
        except sqlite3.Error as e:
            print("Error al modificar la cabaña:", e)
            conn.rollback()
        
        conn.close()
        return changes > 0


def total_a_pagar(cabania_id, fecha_ent, fecha_sal):
    '''
    Función auxiliar que calcula la cantidad de noches de reserva y devuelve el total a pagar considerando el precio por noche de la cabaña elegida.
    '''
    total = None
    conn = get_db_connection()
    if conn is not None:
        fecha_ent = datetime.strptime(fecha_ent, "%Y-%m-%d")
        fecha_sal = datetime.strptime(fecha_sal, "%Y-%m-%d")
        cant_de_noches = (fecha_sal - fecha_ent).days + 1 # Ajuste de +1 para incluir la salida
        query = f"""SELECT precio_noche FROM Cabanias 
                    WHERE cabania_id = ?"""
        res = conn.execute(query, (cabania_id,)).fetchone()
        conn.close()

        precio_noche = res['precio_noche']
        total = cant_de_noches * precio_noche
        total = round(total, 2)
    return total
