from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import traceback

from modules.viewhelper import ViewHelper, FormHelper
from .forms import signupForm

vh = ViewHelper("_site", ["base"])
fh = FormHelper(vh)

def main(request):
    request.session, l = vh.handle_requestdata(request)
    
    params = {"title": "PROJECT_NAME"}

    if request.method == "POST":
        form = fh.populate_form(signupForm(request.POST), l)
        if form.is_valid():
            clfm = form.cleaned_data


            try:
                pass


            
            except Exception as e:
                print(traceback.format_exc(e))
                messages.add_message(request, messages.ERROR, f"Account could not be created. Something went wrong.")
                form.initial=clfm
    else:
        form = fh.populate_form(signupForm(), l)


    params["signupForm"] = form
    return render(request, "main.html", vh.build_params(["main"], params, l))
