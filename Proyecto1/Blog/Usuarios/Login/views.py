from django.shortcuts import render

# Create your views here.
def iniciar(request):
    return render(request,"iniciar.html")