"""
URL configuration for curriculum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import send_json
from .views import json_jobs
from .views import json_skills

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Inicio.as_view(), name='inicio'),
    path('info/', views.Informacion.as_view(), name='info'),
    path('sendjson/', send_json, name='send_json'),
    path('jsonskills/', json_skills, name='json_skills'),
    path('jsonjobs/', json_jobs, name='json_jobs')
]