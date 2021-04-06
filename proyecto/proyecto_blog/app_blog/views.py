from django.shortcuts import render
from app_blog.formulario import FormularioUsuario

# Create your views here.
def index(request):
    return render(request, 'index.html')

def registro(request):
        form = FormularioUsuario()
        return render(request, 'registro.html', {
            'form': form
        })