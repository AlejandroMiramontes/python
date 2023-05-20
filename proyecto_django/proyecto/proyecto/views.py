from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
import json

def index(request):
    
    return HttpResponse("Hola Mundo")

class Inicio(View):
    template_name = "index.html"
    
    def post(self,request):
        return render(request)
    
    def get(self,request):
        nombre = "Alex"
        edad = 34
        return render(request,self.template_name,{
            'nombre': nombre,
            'edad': edad
        })