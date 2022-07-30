from django import forms

class Contact_form(forms.Form):
    name = forms.CharField()
    email_address = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
