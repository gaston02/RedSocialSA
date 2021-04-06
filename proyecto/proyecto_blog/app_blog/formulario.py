from django import forms
from django.core import validators

class FormularioUsuario(forms.Form):
    nombre = forms.CharField(
        label = "Nombre Usuario ",
        max_length = 30,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Gastón'
            }
        ),
    validators = [
            validators.RegexValidator('^[a-zA-Z0-9 ñ]*$', 'El nombre debe ser alfa numerico', 'titulo_invalido')
        ]
    )

    apellido = forms.CharField(
        label = "Apellido Usuario ",
        max_length = 30,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Fuentes'
            }
        ),
    validators = [
            validators.RegexValidator('^[a-zA-Z0-9 ñ]*$', 'El apellido debe ser alfa numerico', 'titulo_invalido')
        ]
    )
    
    mail = forms.EmailField(
        label = "E-mail Usuario ",
        max_length = 50,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'gastonandres.fuentes@gmail.com'
            }
        )
    )

    descripcion = forms.CharField(
        label = "Descripcion Usuario ",
        widget = forms.Textarea 
    )

    facebook = forms.URLField(
        label = "Facebook Usuario "
    )

    instagram = forms.URLField(
        label = "Instagram Usuario "
    )

    twitter = forms.URLField(
        label = "Twitter Usuario "
    )

    tiktok = forms.URLField(
        label = "Tiktok Usuario "
    )

    google_plus = forms.URLField(
        label = "Google Plus Usuario "
    )