from django.shortcuts import render
from django.http import HttpResponse
from .base import build_params, allowed_languages, choose_lang, handle_userdata, populate_form
from .forms import signupForm

def main(request):
    l = choose_lang(request)
    if request.session.get("language") not in allowed_languages:
        request.session["language"] = l
    
    request.session = handle_userdata(request)

    form = populate_form(signupForm())
    params = {"title": "PROJECT_NAME"}

    params["signupForm"] = form
    return render(request, "main.html", build_params(["main"], params, l))
