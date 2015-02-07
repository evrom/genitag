from django import forms


class Title(forms.Form):
    title = forms.CharField(max_length=100)
