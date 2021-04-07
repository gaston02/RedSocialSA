from django import forms
from django.core import validators

class FormularioUsuario(forms.Form):
    nombre = forms.CharField(
        label = "Nombre Usuario ",
        max_length = 30,
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Gastón'
            }
        ),
    validators = [
            validators.RegexValidator('^[a-zA-Z0-9 ñ]*$', 'El nombre debe ser alfa numerico', 'nombre_invalido')
        ]
    )

    apellido = forms.CharField(
        label = "Apellido Usuario ",
        max_length = 30,
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Fuentes'
            }
        ),
    validators = [
            validators.RegexValidator('^[a-zA-Z0-9 ñ]*$', 'El apellido debe ser alfa numerico', 'apellido_invalido')
        ]
    )
    
    mail = forms.EmailField(
        label = "E-mail Usuario ",
        max_length = 50,
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'gastonandres.fuentes@gmail.com'
            }
        )
    )

    descripcion = forms.CharField(
        label = "Descripcion Usuario ",
        widget = forms.Textarea,
        required = False  
    )

    facebook = forms.URLField(
        label = "Facebook Usuario ",
        required = False
    )

    instagram = forms.URLField(
        label = "Instagram Usuario ",
        required = False
    )

    twitter = forms.URLField(
        label = "Twitter Usuario ",
        required = False
    )

    tiktok = forms.URLField(
        label = "Tiktok Usuario ",
        required = False
    )

    google_plus = forms.URLField(
        label = "Google Plus Usuario ",
        required = False
    )