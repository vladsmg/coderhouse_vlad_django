from django.http import HttpResponse

 

def saludo(request):

    return HttpResponse("¡Hola!")

def saludo2(request):
    nombre = input("ingresa tu nombre = ")
    return HttpResponse(f"Hola <h1> {nombre} </h1>")

def nombre(request, nombre,apellido):
    return HttpResponse(f"{nombre.upper()},{apellido}")

def fecha_hora(request):
    from datetime import datetime
    ahora = datetime.now().strftime(r"%d/%m/%Y %H:%M:%S.%f")
    return HttpResponse(ahora)

def tirar_dados(request):
    import random
    numero_dado = random.randint(1,6)
    if numero_dado ==6:
        return HttpResponse(f"<h1> Has tirado el dado : {numero_dado} Felicidades </h1> ")
    else:
        return HttpResponse(F"<h1> Has tirado el dado : {numero_dado} </h1> <br> sigue intentando")
       

    