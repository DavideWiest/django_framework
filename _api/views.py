from django.http import HttpResponse
from .apihelper import UrlQueryManager, BadRequestError
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .apihelper import successful_authentication, AUTH_ERR

@api_view()
def status(request):
    if not successful_authentication(request):
        return Response(AUTH_ERR)

    response = {"status": "ok"}

    return Response(response)