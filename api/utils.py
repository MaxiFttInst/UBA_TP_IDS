from flask import request, jsonify
from functools import wraps
from settings import ADMIN_PASS


def admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        consulta = request.get_json(silent=True)
        if consulta == None:
            return jsonify({"mensaje": "ingrese una clave para realizar esta accion."}), 403
        if "secreto" not in (consulta.keys()):
            return jsonify({"mensaje": "acceso denegado"}), 403
        if consulta["secreto"] != ADMIN_PASS:
            return jsonify({"mensaje": "acceso denegado"}), 403
        return func(*args, **kwargs)
    return wrapper
