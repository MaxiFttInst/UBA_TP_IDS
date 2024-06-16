import calendar
import requests
import os

API_URL = os.environ.get("API_URL", "https://posadabyteados.pythonanywhere.com")
NOMBRES_MESES = {
    "1": "Enero",
    "2": "Febrero",
    "3": "Marzo",
    "4": "Abril",
    "5": "Mayo",
    "6": "Junio",
    "7": "Julio",
    "8": "Agosto",
    "9": "Septiembre",
    "10": "Octubre",
    "11": "Noviembre",
    "12": "Diciembre"
}

def obtener_reservas(cabania_id):
    res = requests.get(f"{API_URL}/cabanias/calendario/{cabania_id}")

    if res.status_code != 200 and res.status_code != 201:
        return {}

    return res.json()

def obtener_calendario(cabania_id:str, mes:int, año:int):
    """
    Retorna una lista con multiples diccionarios. Cada diccionario de la lista
    corresponde a una semana del mes y año enviados por parametro. Cada dia de la semana
    es un diccionario con informacion sobre el numero de dia y si esta ocupado

    Ejemplo:
    [
        {'2024-06-05': {
                'dia': 5,
                'ocupado': False
            }
        },
        {'2024-06-06': {
                'dia': 6,
                'ocupado': True
            }
        }
    ]
    """
    calendario = calendar.Calendar()
    iterador = calendario.itermonthdates(año, mes)
    fechas = [{}]
    dia_de_semana = 0
    semana = 0
    reservas = obtener_reservas(cabania_id)

    for date in iterador:
        if dia_de_semana == 7:
            fechas.append({})
            semana += 1
            dia_de_semana = 0
        dia_de_semana += 1

        date = str(date)
        dia = date.split("-")[2]

        fechas[semana][date] = {
            "dia": dia,
            "ocupado": False
        }

        for reserva in reservas:
            entrada = reserva["fecha_ent"]
            salida = reserva["fecha_sal"]

            if entrada <= date <= salida:
                fechas[semana][date] = {
                    "dia": dia,
                    "ocupado": True
                }

    return fechas

def obtener_proximos_calendarios(cabania_id:str, mes:int, año:int, n:int):
    """
    Llama a obtener_calendario() una cantidad n de veces y devuelve una lista con
    con tuplas que contienen un calendario y el nombre de mes corresponiendte
    """
    calendarios = []

    for i in range(n):
        calendario_data = obtener_calendario(cabania_id, mes, año)
        nombre_mes = NOMBRES_MESES[str(mes)]
        calendarios.append((calendario_data, nombre_mes))
        if mes == 12:
            mes = 1
            año += 1
        else:
            mes += 1

    return calendarios