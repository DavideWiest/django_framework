from django.urls import path
from django.shortcuts import render
from .base import build_params, choose_lang

def terms(request):
    
    l = choose_lang(request)
    if lang not in ("de", "ch", "au"):
        lang = "en"
    else:
        lang = "de"
    return render(request, f"legal/{l}_terms.html", build_params("", ["credentials", "legal"], {}, l))

def impressum(request):
    
    l = choose_lang(request)
    if lang not in ("de", "ch", "au"):
        lang = "en"
    else:
        lang = "de"
    return render(request, f"legal/{l}_impressum.html", build_params("", ["credentials", "legal"], {}, l))




urlpatterns = [
    path("agb/", terms),
    path("terms/", terms),
    path("impressum/", impressum),
    path("datenschutzerklärung/", impressum),
    path("privacystatement/", impressum)
]