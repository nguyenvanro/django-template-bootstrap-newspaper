import re
from django import forms
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse, request
from Service.forms import ContactForm
# Create your views here.

def ContactView(request):
    
    if request.method == 'POST' and request.is_ajax():
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            return JsonResponse({'name':name}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors':errors},status=400)
    else:
        return render(request, 'contact/contact.html')

