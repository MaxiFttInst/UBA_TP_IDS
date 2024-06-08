import os
import sqlite3
NOMBRE_BASE  = 'hosteria_byteados.db'
#Este modelo presupone que la base de datos se encuentra en el directorio padre de este script <en caso de necesidad, modificar>

# Obtener la ruta absoluta del directorio donde se encuentra el script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Obtener la ruta del directorio padre (un nivel arriba)
parent_dir = os.path.dirname(script_dir)

db_path = os.path.join(parent_dir, NOMBRE_BASE)

def get_db_connection():
    '''
    Devuelve cursor de conexión a la base de datos según la RUTA_BD
    '''
    if not os.path.exists(db_path):
        print(f"Falló la conexión a la base de datos \nEl archivo de la base de datos no existe en la ruta: {db_path}")
        return None
    conn = sqlite3.connect(db_path) #Conexion a base
    conn.row_factory = sqlite3.Row # Para obtener un diccionario en lugar de una tupla
    cursor = conn.cursor() #Cursor
    return cursor


def correr_prueba(nombre_tabla = None):
    '''
    Corre prueba de la ruta de la base de datos, si se pasa el nombre_tabla también verifica si existe.
    '''
    print(f"Ruta asignada de la base de datos: {db_path}")
    # Verificar si el archivo de la base de datos existe
    if not os.path.exists(db_path):
        print(f"El archivo de la base de datos no existe en la ruta: {db_path}")
    else:
        # Conectar a la base de datos
        conn = sqlite3.connect(db_path)

        # Crear un cursor
        cursor = conn.cursor()

        # Consultar la lista de tablas para verificar que la tabla existe
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tablas = cursor.fetchall()
        print("Tablas en la base de datos:", tablas)

        # Asegúrate de que la tabla que estás intentando consultar aparece en la lista
        nombre_tabla = 'nombre_de_tu_tabla'  # Reemplaza esto con el nombre real de tu tabla

        if (nombre_tabla,) in tablas:
            # Si la tabla existe, realiza la consulta
            cursor.execute(f'SELECT * FROM {nombre_tabla}')
            filas = cursor.fetchall()

            for fila in filas:
                print(fila)
        else:
            print(f"La tabla '{nombre_tabla}' no existe en la base de datos.")

        # Cerrar la conexión
        conn.close()

def devolver_current_path():
    return script_dir
