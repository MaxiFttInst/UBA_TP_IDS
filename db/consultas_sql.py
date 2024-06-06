import sqlite3
from datetime import datetime

RUTA_BD = "hosteria_byteados.db"

def get_db_connection():
    conn = sqlite3.connect(RUTA_BD)
    conn.row_factory = sqlite3.Row # Para obtener un diccionario en lugar de una tupla
    return conn

def obtener_cabanias():
    conn = get_db_connection()
    cabanias = conn.execute("SELECT * FROM Cabanias").fetchall()
    conn.close()
    res = {}
    for cabania in cabanias:
        res[cabania["cabania_id"]] = {
            "nombre": cabania["nombre"],
            "cap_max": cabania["cap_max"],
            "descripcion": cabania["descripcion"],
            "precio_noche": cabania["precio_noche"]}
    return res

def imagenes_de_cabania(cabania_id):
    conn = get_db_connection()
    imagenes = conn.execute(f"SELECT descripcion, imagen_link FROM Imagenes WHERE cabania_id = '{cabania_id}'").fetchall()
    conn.close()
    res = {}
    for imagen in imagenes:
        res[imagen["descripcion"]] = imagen["imagen_link"]
    return res

def consultar_disponibilidad(cabania_id, fecha_ent, fecha_sal):
    conn = get_db_connection()
    query = f"""
    SELECT COUNT(*) FROM Reservas
    WHERE (
        (cabania_id = '{cabania_id}') AND
        ('{fecha_ent}' <= fecha_sal AND '{fecha_sal}' >= fecha_ent)
        )
    """
    res = conn.execute(query).fetchone()
    conn.close()
    return res[0] == 0

def calendario_reservas(cabania_id):
    conn = get_db_connection()
    query = f"""
    SELECT fecha_ent, fecha_sal FROM Reservas
    WHERE cabania_id = '{cabania_id}'
    """
    res = conn.execute(query).fetchall()
    conn.close()

    reservas = []
    for row in res:
        reserva = {
            "fecha_ent": row["fecha_ent"],
            "fecha_sal": row["fecha_sal"]
        }
        reservas.append(reserva)

    return reservas

def total_a_pagar(cabania_id, fecha_ent, fecha_sal):
    fecha_ent = datetime.strptime(fecha_ent, "%Y-%m-%d")
    fecha_sal = datetime.strptime(fecha_sal, "%Y-%m-%d")
    cant_de_noches = (fecha_sal - fecha_ent).days + 1 # Ajuste de +1 para incluir la salida
    conn = get_db_connection()
    query = f"SELECT precio_noche FROM Cabanias WHERE cabania_id = '{cabania_id}'"
    res = conn.execute(query).fetchone()
    conn.close()
    precio_noche = res['precio_noche']
    total = cant_de_noches * precio_noche
    return round(total, 2)

def realizar_reserva(cabania_id, fecha_ent, fecha_sal, id_cliente, nombre_completo_cliente, telefono_cliente, mail_cliente):
    if not consultar_disponibilidad(cabania_id, fecha_ent, fecha_sal):
        return False

    conn = get_db_connection()
    precio_total = total_a_pagar(cabania_id, fecha_ent, fecha_sal)
    conn.execute(
        """INSERT INTO reservas (cabania_id, fecha_ent, fecha_sal, id_cliente, nombre_completo_cliente, telefono_cliente, mail_cliente, precio_total)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (cabania_id, fecha_ent, fecha_sal, id_cliente, nombre_completo_cliente, telefono_cliente, mail_cliente, precio_total)
    )
    conn.commit()
    reserva_codigo = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
    conn.close()
    return reserva_codigo

def consultar_reserva(dni_cliente, telefono_cliente, mail_cliente):
    """
    Podría devolver:
    {
    reserva_codigo1: {fecha_ent: str, fecha_sal: str},
    reserva_codigo2: { ... }
    ...
    }
    """
    return

def eliminar_reserva(reserva_codigo):
    conn = get_db_connection()
    conn.execute(f"DELETE FROM Reservas WHERE reserva_codigo = {reserva_codigo}")
    changes = conn.total_changes
    conn.commit()
    conn.close()
    return changes > 0