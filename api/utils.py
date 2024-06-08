from flask import request, jsonify
from functools import wraps
from settings import ADMIN_PASS

def admin(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        consulta = request.get_json()
        if consulta["secreto"] != ADMIN_PASS:
            return jsonify({"mensaje":"acceso denegado"}), 403
        return func(*args, **kwargs)
    return wrapper
