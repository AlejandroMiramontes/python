from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from django.http import JsonResponse

class Informacion(View):
    template_name = "info.html"

    def post(self,request):
        return render(request)

    def get(self,request):    
        datos = {"nombres": "Alejandro", 
                "primer_apellido": "Miramontes",
                "segundo_apellido": "Rivas",
                "fecha_nacimiento": "04/14/1989",
                "celular": 6142869003,
                "correo": "alejandro.miramontes@oracle.com",
                "domicilio": "Av. Empresarios 135-Piso 4, Puerta de Hierro, 45116 Zapopan, Jal.",
                "genero": "Masculino",
                "objetivo": "Aprender python",
                "salario_esperado": "$150,000"} 
        
        #Imprimir en pantalla el diccionario datos:
        print("\nDiccionario de datos personales:\n")   
        for keys, value in dict(datos).items():
            print(value)
        
        skills = ["Oracle Database Administrator", 
                  "Python Begginer", 
                  "Team Leadership",
                  "English Proficency"]
        
        #Imprimir en pantalla la lista skills:
        print("\nLista de habilidades:\n")
        for i in range(len(skills)):
                print(skills[i])
            
        trabajos = {
                (1, "Oracle") : {"fecha_inicio" : 2022, "fecha_fin" : "Actual", "Puesto" : "System 3-Analyst"}, 
                (2, "BMC") : {"fecha_inicio" : 2022, "fecha_fin" : 2022, "Puesto" : "Technical Support Specialist"},
                (3, "TCS") : {"fecha_inicio" : 2019, "fecha_fin" : 2022, "Puesto" : "Technical Support Analyst"}
                }
        
        #Imprimir en pantalla el diccionario trabajos:
        print("\nDiccionario de trabajos:\n")    
        for keys, value in dict(trabajos).items():
            print(value)
                                    
        return render(request,self.template_name,{'data':datos,
                                                  'trabajos':trabajos,
                                                  'skills':skills})

class Inicio(View):
    template_name = "index.html"
    def post(self,request):
        return render(request)
    
    def get(self,request):
        return render (request,self.template_name)
                   
# Generación de archivos json.

def send_json(request):

    data = [{"nombres": "Alejandro", 
                "primer_apellido": "Miramontes",
                "segundo_apellido": "Rivas",
                "fecha_nacimiento": "04/14/1989",
                "celular": 6142869003,
                "correo": "alejandro.miramontes@oracle.com",
                "domicilio": "Av. Empresarios 135-Piso 4, Puerta de Hierro, 45116 Zapopan, Jal.",
                "genero": "Masculino",
                "objetivo": "Aprender python",
                "salario_esperado": "$150,000"}]
    
    return JsonResponse(data, safe=False)

def json_skills(request):
    skills = ["Oracle Database Administrator", 
                  "Python Begginer", 
                  "Team Leadership",
                  "English Proficency"]
    
    return JsonResponse(skills, safe=False)
    
    
def json_jobs(request):
    jobs = [{
            ("Oracle") : {"fecha_inicio" : 2022, "fecha_fin" : "Actual", "Puesto" : "System 3-Analyst"}, 
            ("BMC") : {"fecha_inicio" : 2022, "fecha_fin" : 2022, "Puesto" : "Technical Support Specialist"},
            ("TCS") : {"fecha_inicio" : 2019, "fecha_fin" : 2022, "Puesto" : "Technical Support Analyst"}
            }]
    
    return JsonResponse(jobs, safe=False)