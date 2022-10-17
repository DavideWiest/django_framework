from django.urls import path
from django.shortcuts import render
from modules.viewhelper import ViewHelper

vh = ViewHelper("legal")

def terms(request):
    
    l = vh.choose_lang(request)
    if lang not in ("de", "ch", "au"):
        lang = "en"
    else:
        lang = "de"
    return render(request, f"legal/{l}_terms.html", vh.build_params(["b_credentials"], {}, l))

def impressum(request):
    
    l = vh.choose_lang(request)
    if lang not in ("de", "ch", "au"):
        lang = "en"
    else:
        lang = "de"
    return render(request, f"legal/{l}_impressum.html", vh.build_params(["b_credentials"], {}, l))




urlpatterns = [
    path("agb/", terms),
    path("terms/", terms),
    path("impressum/", impressum),
    path("datenschutzerklärung/", impressum),
    path("privacystatement/", impressum)
]