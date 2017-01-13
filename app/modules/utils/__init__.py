from app import db
import sqlalchemy, json, os
from functools import wraps
from flask import jsonify, request, session


APP_ROOT = os.path.dirname(os.path.realpath(__file__))
# LOG_FILENAME = "rebates_log"


NOT_AUTHENTICATED_ERROR = 'You must be logged in to access this route!'
NOT_AUTHORIZED_ERROR = 'You do not have premission to access this route!'
LOGGED_IN_KEY = "logged_in"


def authenticate():
    session[LOGGED_IN_KEY] = True


def deauthenticate():
    session[LOGGED_IN_KEY] = False

def is_authenticated():
    return session.get(LOGGED_IN_KEY, False)

def is_admin():
    return (session.get('role', 'client') == "admin")


def get_my_ip(request):
    return request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  


def obj_to_dict(o):
    if o is not None:            
        state = sqlalchemy.inspect(o)
        if state.persistent:
            db.session.refresh(o)
        return dict((k, v) for k, v in o.__dict__.iteritems() if k[0] != '_')
    return None

def format_jsend_response(data=None, status="success", message=None, code=None):
    if status == "success" or status == "fail":
        if data is None:
            raise ValueError(
                "data can't be None when status is set to success.")
        else:
            response = {"status": status, "data": data}
    elif status == "error":
        if message is None:
            raise ValueError(
                "message can't be None when status is set to error")
        else:
            response = {"status": status, "data": data, "message": message,
                        "code": code}
    else:
        raise ValueError(
            "Invalid value for status. Valid values are success, fail and error")

    response = dict((k, v) for k, v in response.iteritems() if v is not None)
    return jsonify(**response)      


def requires_auth(*roles):
    def wrapper(f):
        @wraps(f)
        def is_logged_in(*args, **kwargs):
            authenticated = session.get(LOGGED_IN_KEY, False)
            print session.get('role') in roles
            if not authenticated:
                return format_jsend_response(status="error", message=NOT_AUTHENTICATED_ERROR)
            else:
                if session.get('role') in roles:
                    return f(*args, **kwargs) 
                return format_jsend_response(status="error", message=NOT_AUTHORIZED_ERROR)
        return is_logged_in    
    return wrapper  