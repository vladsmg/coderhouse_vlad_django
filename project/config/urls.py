"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

from .views import saludo,saludo2, nombre, fecha_hora , tirar_dados

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('saludo/', saludo),
    #path('saludo2/', saludo2),
    #path('nombre/<nombre>/<apellido>', nombre),
    #path('fecha_hora/', fecha_hora),
    #path('tirar_dados/', tirar_dados)
    path("", include("core.urls"))
]
