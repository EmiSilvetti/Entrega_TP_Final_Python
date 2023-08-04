from django.shortcuts import render
from Blog_Python.models import Entrada,Comentario

# Create your views here.
def home(request):
    Blog_Python = Entrada.objects.all()
    if request.method == "POST":
        nombre = request.POST["nombre"] 
        mensaje = request.POST["mensaje"] 
        obj = Comentario(nombre=nombre,Comentario=mensaje)
        obj.save()
        mensaje = "Gracias por tu comentario"
        return render(request,"bienvenida.html",{"Blog_Python":Blog_Python,"mensaje":mensaje})
    return render(request,"bienvenida.html",{"Blog_Python":Blog_Python})