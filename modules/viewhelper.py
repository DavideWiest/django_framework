from django.utils import translation
from django import forms
import json



class ViewHelper():
    def __init__(self, base_path, omni_content_files=[]):
        self.base_path = base_path
        self.omni_content_files = omni_content_files + ["b_data"]
        self.std_title_clause = " - FINsights"
        self.lang_independant_files = ("credentials", "data", "b_credentials", "b_data")
        self.allowed_languages = ("en", "de")
        self.base_content_files = ("b_credentials", "b_data")
           
    def openfile(self, filename, subfield=None):
        if filename.split(".")[0] in self.base_content_files:
            filepath = f"_base_static/_content/{filename}"
        else:
            filepath = f"{self.base_path}/static/_content/{filename}"
        with open(filepath, "r", encoding="utf-8") as f:
            file = json.load(f)
            if subfield:
                file = file.get(subfield, file)

        return file

    def build_params(self, storage_ptrs, params, language):
        
        c_files = {}
        for storage_ptr in storage_ptrs + self.omni_content_files:
            if storage_ptr != "":
                if "/" in storage_ptr:
                    filename, subfield = storage_ptr.split("/")
                else:
                    filename, subfield = (storage_ptr, "")
                
                c_files[filename + "_" + subfield.capitalize() if subfield != "" else filename] = self.openfile(language + "/" + filename + ".json" if filename not in self.lang_independant_files else filename + ".json", subfield=subfield if subfield != "" else None)
            else:
                c_files[filename] = {}

        bparams = {
            "title": params.get("title", "") + self.std_title_clause,
            "base_url": "http://127.0.0.1:8000/",
            "c": c_files,
            "l": language
        }

        return {**bparams, **params}

    def choose_lang(self, request):
        language = translation.get_language_from_request(request)

        # first priority
        if request.method == "GET":
            if request.GET.get("language") in self.allowed_languages:
                # change request.session["language"]
                # change db user settings.language
                return request.GET.get("language")
        
        # second priority
        if "user_id" in request.session:
            # change request.session["language"]
            pass
        
        # third priority
        if request.session["language"] in self.allowed_languages:
            return request.session["language"]
        
        # allow only de or en
        if language in ("ch", "au"):
            language = "de"
        if language != "de":
            language = "en"

        # language = "en"

        return language


        
    def getip(self, request):
        user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
        if user_ip_address:
            ip = user_ip_address.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def choose_lang(self, request):
        if request.method == "GET":
            if request.session.get("language") in self.allowed_languages:
                request.session["language"] = request.session.get("language")
                return request.session, request.session["language"]
        
        
        language = translation.get_language_from_request(request)

        if language in ("ch", "au"):
            language = "de"
        if language != "de":
            language = "en"

        return request.session, language

    def handle_requestdata(self, request, l):
        request.session, l = self.choose_lang(request)
            
        if "language" in request.sesison and request.session.get("language") not in self.allowed_languages:
            del request.session["language"]

        return request.session, l

class FormHelper():
    def __init__(self, viewhelper):
        self.vh = viewhelper

    def populate_form_labels(self, form_obj: forms.Form, l):
        form_name = form_obj.__class__.__name__
        
        form_fields = self.vh.openfile(l + "/forms.json", form_name).get("labels")
        if form_fields != None:
            for field in form_fields:
                form_obj.fields[field].label = form_fields[field]
            
        return form_obj

    def populate_form_choices(self, form_obj: forms.Form, l):
        form_name = form_obj.__class__.__name__

        form_fields = self.vh.openfile(l + "/forms.json", form_name).get("choices")
        if form_fields != None:
            for field in form_fields:
                form_obj.fields[field].choices = [(k, v) for k, v in form_fields[field].items()]
            
        return form_obj

    def populate_form_help_text(self, form_obj: forms.Form, l):
        form_name = form_obj.__class__.__name__

        form_fields = self.vh.openfile(l + "/forms.json", form_name).get("help_text")
        if form_fields != None:
            for field in form_fields:
                form_obj.fields[field].help_text = form_fields[field]

        return form_obj

    def populate_form(self, form_obj: forms.Form, l):
        form_obj = self.populate_form_labels(form_obj, l)
        form_obj = self.populate_form_choices(form_obj, l)
        # form_obj = self.populate_form_help_text(form_obj, l)
        return form_obj


def prebuild_params(request, params):
    params["navbar_show_type"] = "old" if "user_id" in request.session else "new"

    # more, like getting name or navigation options

    return params
