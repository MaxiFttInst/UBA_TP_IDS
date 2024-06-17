from db.consultas.conexion_base import get_db_connection
from db.consultas.cabania_consultas_sql import total_a_pagar, consultar_disponibilidad
import sqlite3
import sys
import os

# Añadir el directorio del paquete a sys.path de manera dinámica
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))


def realizar_reserva(cabania_id, fecha_ent, fecha_sal, id_cliente, nombre_completo_cliente, telefono_cliente, mail_cliente):
    '''
    Realiza la reserva de la habitación.
    Si se realiza correctamente, devuelve el código de reserva generado, en caso contrario devuelve False.

    PRE-CONDICIONES:
    Las fechas deben tener formato válido
    '''
    if not consultar_disponibilidad(cabania_id, fecha_ent, fecha_sal):
        return False

    cambios = 0
    conn = get_db_connection()

    if conn is not None:
        precio_total = total_a_pagar(cabania_id, fecha_ent, fecha_sal)
        query = """Insert into Reservas(cabania_id, fecha_ent, fecha_sal, id_cliente, nombre_completo_cliente, telefono_cliente, mail_cliente, precio_total) values 
                    (?, ?, ?, ?, ?, ?, ?, ?)"""
        conn.execute(query, (cabania_id, fecha_ent, fecha_sal, id_cliente,
                     nombre_completo_cliente, telefono_cliente, mail_cliente, precio_total))
        conn.commit()

        cambios = conn.total_changes
        reserva_codigo = conn.execute(
            "SELECT last_insert_rowid()").fetchone()[0]
        conn.close()

    return reserva_codigo if cambios > 0 else False


def consultar_reservas(dni_cliente, nombre_cliente):
    '''
    Consulta si el cliente ya tiene reservas y devuelve sus datos. 
    Si todos los datos coinciden, devuelve una tupla con los códigos de reserva. 
    En caso contrario devuelve False.
    '''
    if not dni_cliente and not nombre_cliente:
        return False

    conn = get_db_connection()
    query = """SELECT r.reserva_codigo, c.nombre, r.fecha_ent, r.fecha_sal, r.mail_cliente from Reservas r, Cabanias c 
                           WHERE r.cabania_id = c.cabania_id 
                                AND lower(r.id_cliente) = lower(?) 
                                AND lower(r.nombre_completo_cliente) = lower(?)"""
    res = conn.execute(query, (dni_cliente, nombre_cliente)).fetchall()
    conn.close()

    return res if res else False

def consultar_reservas_todas():
    '''
    Consulta todas las reservas que estan en base de datos. 
    Devuelve "False" si no hay reservas.
    '''
    conn = get_db_connection()
    query = """SELECT * FROM Reservas;"""
    res = conn.execute(query).fetchall()
    conn.close()

    return res if res else False

def actualizar_reserva(id, datos : dict):
    """
    Actualiza los datos de la reserva segun el id proporcionado.
    Recibe también un dict con los datos
    """
    if not id:
        return False
    
    conn = get_db_connection()
    changes = 0
    if conn is not None:
        valores = []
        columnas = []

        query = "UPDATE Reservas SET "
        for key, value in datos.items():
            columnas.append(key + " = ?")
            valores.append(value)

        columnas = ", ".join(columnas)

        query += columnas
        query += f" WHERE reserva_codigo = {id}"

        try:
            conn.execute(query, tuple(valores))
            conn.commit()
            changes = conn.total_changes

        except sqlite3.Error as e:
            print("Error al modificar la reserva:", e)
            conn.rollback()
    
    return changes > 0
        
def eliminar_reserva(reserva_codigo = None, email = None):
    '''
    Elimina la reserva elegida según el código de reserva y mail del cliente.
    Si la operación es exitosa devuelve True, caso contrario False.

    Pre-condiciones:
        - Los argumentos 'reserva_codigo' y 'email' deben ingresarse simultaneamente.
    '''
    argumentos = []
    conn = get_db_connection()

    if conn is not None:
        if reserva_codigo is not None and email is not None:
            query = "DELETE from Reservas WHERE reserva_codigo = ? AND mail_cliente = ?"
            argumentos.append(reserva_codigo)
            argumentos.append(email)
        
        conn.execute(query, tuple(argumentos))
        conn.commit()

        changes = conn.total_changes
        
        conn.close()
    return changes > 0
