from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.A

class Usuario(User):
    imagen = models.ImageField(upload_to='usuario', default='usuario\default-user.png')
    # imagen = CloudinaryField(null=True, blank=True , verbose_name='Imagen')

    def get_absolute_url(self):
        return reverse('index')