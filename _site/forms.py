from django import forms


class signupForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"id": "", "class": ""}))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={"id": "", "class": ""}))
    group = forms.ChoiceField(widget=forms.RadioSelect(attrs={"id": "", "class": ""}))

