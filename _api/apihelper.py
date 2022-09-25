import urllib
import json



AUTH_ERR = {"status": "error", "error": "Wrong/No authentication token"}

def successful_authentication(request):
    # handle authorization here

    return True

class BadRequestError(Exception):
    pass

class UrlQueryManager:
    def __init__(self, request):
        self.request = request

    def get_bool_param(self, name, optional=True, default=False):
        try:
            arg = self.request.query_params.get(name)

            arg = arg in ("True", "true", True)
        except:
            if not optional:
                raise BadRequestError(f"Query paramater {name} was not found in URL and is not optional")
            else:
                arg = default

        return arg

    def get_num_param(self, name, optional=True, default=False, max=0, min=0, isint=False):
        try:
            num = float(self.request.query_params.get(name))

        except:
            if not optional:
                raise BadRequestError(f"Query paramater {name} was not found in URL and is not optional")
            else:
                arg = default

        if isint:
            try:
                num = int(num)
            except:
                raise BadRequestError(f"Query paramater {name} must be an integer")

        if bool(max):
            num = min(max, num)
        if bool(min):
            num = max(min, num)
            
        return arg
    
    def get_json_param(self, name, optional=False, default={}):
        try:
            qparam = self.request.query_params.get(name)

            try:
                arg = urllib.parse.unquote(qparam)
                arg = urllib.parse.unquote_plus(arg)
                arg = json.loads(arg)
            except Exception as e:
                raise e
        except:
            if not optional:
                raise BadRequestError(f"Query paramater {name} was not found in URL and is not optional")
            else:
                arg = default
        
        return arg
