from django import forms
from django.db import models
from django.forms import fields
from Service.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        models = Contact
        fields = "__all__"