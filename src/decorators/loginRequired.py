from functools import wraps
from flask import abort, request
import jwt


def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kargs):
        if "Authorization" not in request.headers:
            abort(401)
        data = request.headers["Authorization"]
        token = str.replace(str(data), "Bearer ", "")
        try:
            jwt.decode(token, "SECRET_KEY", algorithms=["HS256"])
        except Exception:
            abort(401)

        return f(*args, **kargs)

    return decorated_function
