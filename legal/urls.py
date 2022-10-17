from django.urls import path
from django.shortcuts import render
from modules.viewhelper import ViewHelper

vh = ViewHelper("legal", [])

def terms(request):
    
    l = vh.choose_lang(request)
    if l not in ("de", "ch", "au"):
        l = "en"
    else:
        l = "de"
    return render(request, f"{l}_terms.html", vh.build_params(["b_credentials"], {}, l))

def impressum(request):
    
    l = vh.choose_lang(request)
    if l not in ("de", "ch", "au"):
        l = "en"
    else:
        l = "de"
    return render(request, f"{l}_impressum.html", vh.build_params(["b_credentials"], {}, l))




urlpatterns = [
    path("agb/", terms),
    path("terms/", terms),
    path("impressum/", impressum),
    path("datenschutzerklärung/", impressum),
    path("privacystatement/", impressum)
]