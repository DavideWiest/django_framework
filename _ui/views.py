from django.shortcuts import render
from django.http import HttpResponse
from .sitehelper import build_params


def main(request):
    
    params = {
        "title": "Davide Wiest"
    }

    return render(request, "main.html", build_params("", params))

def projects(request):
    
    params = {
        "title": "Davide Wiest"
    }

    return render(request, "projects.html", build_params("Projekte", params))
