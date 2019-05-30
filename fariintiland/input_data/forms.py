from django import forms

class ContactForm(forms.Form):
    integer_field = forms.IntegerField()