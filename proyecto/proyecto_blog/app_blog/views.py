from django.shortcuts import render, redirect
from app_blog.formulario import FormularioUsuario
from app_blog.models import Autor

# Create your views here.
def index(request):
    return render(request, 'index.html')

def registro(request):
        form = FormularioUsuario()
        return render(request, 'registro.html', {
            'form': form
        })

def crear_autor(request):
    if(request.method=='POST'):
        form = FormularioUsuario(request.POST)
        if(form.is_valid):
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            correo = request.POST['mail']
            descripcion = request.POST['descripcion']
            fb = request.POST['facebook']
            insta = request.POST['instagram']
            twitter = request.POST['twitter']
            tiktok = request.POST['tiktok']
            google = request.POST['google_plus']
            autor = Autor(
                nombre = nombre,
                apellido = apellido,
                email = correo,
                descripcion = descripcion,
                facebook = fb,
                instagram = insta,
                twitter = twitter,
                tiktok = tiktok,
                googlePlus = google
            )
            autor.save()
            return redirect('index')
    else:
        form = FormularioUsuario()
    return render(request, 'registro.html',{
        'form':form
    })

def login(request):
    return render(request, 'login.html')