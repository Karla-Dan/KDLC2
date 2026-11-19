from django.shortcuts import render

def inicio(request):
    return render(request, "Lazo/inicio.html")
def registro(request):
    return render(request, "Lazo/formregistro.html")