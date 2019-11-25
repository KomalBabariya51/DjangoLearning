from django import forms


class Loginform(forms.Form):
    name = forms.CharField(label="Enter your name", max_length=20)
    email = forms.EmailField(max_length=30)
    text = forms.CharField(widget=forms.Textarea)