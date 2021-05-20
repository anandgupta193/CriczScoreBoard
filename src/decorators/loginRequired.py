
from functools import wraps
from flask import abort , request
import jwt

def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kargs):
        if not 'Authorization' in request.headers:
            abort(401)
        user = None
        data = request.headers['Authorization']
        token = str.replace(str(data), 'Bearer ','')
        try:
            jwt.decode(token, 'SECRET_KEY', algorithms=['HS256'])
        except:
            abort(401)

        return f(*args, **kargs)            
    return decorated_function