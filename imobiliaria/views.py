from django.shortcuts import render
from .models import Imovel
def home(request):
    context = {
        'imoveis': Imovel.objects.all()
    }
    return render (request,'imobiliaria/home.html',context)
