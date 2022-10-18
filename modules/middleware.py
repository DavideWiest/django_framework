from modules.viewhelper import ViewHelper

vh = ViewHelper("_site")

class registrationMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_request(self,request):
        if request.session.get("language") not in vh.allowed_languages:
            request.session["language"] = vh.choose_lang(request)
        return None

    # def process_response(self,request,response):
    #     return None
