from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import traceback

from .base import build_params, allowed_languages, choose_lang, handle_userdata, populate_form
from .forms import signupForm

def main(request):
    l = choose_lang(request)
    if request.session.get("language") not in allowed_languages:
        request.session["language"] = l
    
    request.session = handle_userdata(request)

    params = {"title": "PROJECT_NAME"}

    if request.method == "POST":
        form = populate_form(signupForm(request.POST), l)
        if form.is_valid():
            clfm = form.cleaned_data




            try:
                pass


            
            except Exception as e:
                print(traceback.format_exc(e))
                messages.add_message(request, messages.ERROR, f"Account could not be created. Something went wrong.")
                form.initial=clfm
    else:
        form = populate_form(signupForm(), l)

    params["signupForm"] = form
    return render(request, "main.html", build_params(["main"], params, l))
