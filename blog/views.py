from django.shortcuts import render
def inicio(request):
    return render(request, 'blog/inicio.html')

def contacto(request):
    return render(request, 'blog/contacto.html')

def servicio(request):
    return render(request, 'blog/servicio.html')