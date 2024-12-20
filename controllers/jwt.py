from jwt import encode, decode, exceptions
from configs.config import SECRET_KEY
from datetime import datetime, timedelta
from flask import jsonify

#calcular expiracion de token
def expiracion_token(days: int):
    now = datetime.now()
    new_day = now + timedelta(days)
    return new_day

#crear token
def crear_token(data: dict):
    token = encode(payload={**data, 'exp':expiracion_token(2)}, key=SECRET_KEY, algorithm="HS256")
    return token.encode('utf-8')

#validar token
def validar_token(token, output=False):
    try:
        if output:
            return decode(token, key=SECRET_KEY, algorithms=["HS256"])
    except exceptions.DecodeError:
        response = jsonify({"mensage":"Token Invalido"})
        response.status_code = 401
        return response
    except exceptions.ExpiredSignatureError:
        response = jsonify({"mensage":"Token Expirado"})
        response.status_code = 401
        return response