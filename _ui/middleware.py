from .base import choose_lang

class registrationMiddleware(object):

    def process_request(self,request):
        request.session["lang"] = choose_lang(request)
        return None

    # def process_response(self,request,response):
    #     return None
