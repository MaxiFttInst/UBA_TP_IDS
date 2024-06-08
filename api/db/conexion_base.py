import os
import sqlite3
NOMBRE_BASE  = 'hosteria_byteados.db'
# Obtener la ruta absoluta del archivo de la base de datos basado en la ubicación del script
script_dir = os.path.dirname(os.path.abspath(__file__))  # Directorio donde se encuentra el script
db_path = os.path.join(script_dir, NOMBRE_BASE)

def get_db_connection():
    '''
    Devuelve cursor de conexión a la base de datos según la RUTA_BD
    '''
    if not os.path.exists(db_path):
        print(f"El archivo de la base de datos no existe en la ruta: {db_path}")
        return None
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row # Para obtener un diccionario en lugar de una tupla
    return conn
