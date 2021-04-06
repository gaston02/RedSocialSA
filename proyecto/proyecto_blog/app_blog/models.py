from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Base(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.BooleanField('Estado', default=True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)
    fecha_modificacion = models.DateField('Fecha de Modificacion', auto_now=True, auto_now_add=False)
    fecha_eliminacion = models.DateField('Fecha de Eliminacion', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True

class Categoria(Base):
    nombre = models.CharField('Nombre de la categoria', max_length=30, unique=True)
    imagen = models.ImageField('Imagen de la categoria', upload_to='categoria/')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

class Autor(Base):
    nombre = models.CharField('Nombre del autor', max_length=30)
    apellido = models.CharField('Apellido del autor', max_length=30)
    email = models.EmailField('Mail del autor', max_length=50)
    descripcion = models.TextField('Descripcion del autor', null = True, blank = True)
    facebook = models.URLField('Facebook del autor', null = True, blank = True)
    instagram = models.URLField('Instagram del autor', null = True, blank = True)
    twitter = models.URLField('Twitter del autor', null = True, blank = True)
    tiktok = models.URLField('Tiktok del autor', null = True, blank = True)
    googlePlus = models.URLField('GooglePlus del autor', null = True, blank = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return '{0}{1}'.format(self.nombre, self.apellido)

class Post(Base):
    titulo = models.CharField('Titulo del post', max_length=50, unique=True)
    slug = models.CharField('Slug', max_length=200, unique=True)
    descripcion = models.TextField('Descripcion del post')
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    categoira = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    contenido = RichTextField()
    imagen = models.ImageField('Imagen referencial', upload_to='imagenes/', max_length=300)
    publicado = models.BooleanField('Publicado / No Publicado', default=False)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    def __str__(self):
        return self.titulo

class Web(Base):
    nosotros = models.TextField('Nosotros')
    telefono = models.CharField('Telefono', max_length=15)
    email = models.EmailField('Mail empresarial', max_length=50)
    direccion = models.CharField('Direccion empresarial', max_length=50)

    class Meta:
        verbose_name = 'Web'
        verbose_name_plural = 'Web'

    def __str__(self):
        return self.nosotros

class RedSocial(Base):
    facebook = models.URLField('Facebook empresarial')
    instagram = models.URLField('Instagram empresarial')
    googlePlus = models.URLField('GooglePlus empresarial')

    class Meta:
        verbose_name = 'Red social'
        verbose_name_plural = 'Redes sociales'
    
    def __str__(self):
        return self.facebook

class Contacto(Base):
    nombre = models.CharField('Nombre', max_length=30)
    apellido = models.CharField('Apellido', max_length=30)
    email = models.EmailField('Mail', max_length=50)
    asunto = models.CharField('Asunto', max_length=50)
    mensaje = models.TextField('Mensaje')

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
    
    def __str__(self):
        return self.asunto

class Suscriptor(Base):
    email = models.EmailField('Mail', max_length=50)

    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'

    def __str__(self):
        return self.email