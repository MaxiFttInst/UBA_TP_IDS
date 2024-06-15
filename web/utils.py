import calendar
import requests
import datetime
from settings import API_URL
# API_URL = os.environ.get("API_URL", "https://posadabyteados.pythonanywhere.com")


def obtener_calendario(cabania_id, mes=None, año=None):
    tiempo = datetime.date.today()
    if año is None:
        año = tiempo.year

    if mes is None:
        mes = tiempo.month
    elif mes > 12:
        mes = 1
        año += 1
    elif mes < 1:
        mes = 12
        año -= 1

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
    return mes, año, fechas


def obtener_reservas(cabania_id):
    res = requests.get(f"{API_URL}/cabanias/calendario/{cabania_id}")

    if res.status_code != 200 and res.status_code != 201:
        return {}

    return res.json()
