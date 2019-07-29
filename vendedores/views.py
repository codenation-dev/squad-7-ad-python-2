from django.shortcuts import render
from django.http import HttpResponse
import vendedores.templates
import datetime

def home(request):
    now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    return render (request, 'vendedores/home.html')#HttpResponse(html)

def plano(request):
    return render(request, 'planos/home.html')