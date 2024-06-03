from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine('sqlite:////ruta/a/db.db')

def obtener_reservas():
    with engine.connect() as conn:
        resultado = conn.execute(text("QUERY"))
    return resultado.all()

def obtener_habitaciones():
    pass