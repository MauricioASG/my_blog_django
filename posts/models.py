from django.db import models

# creamos una clase para el modelo
class Post(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  order = models.IntegerField() #Agregamos nuevo campo
  created_at = models.DateField(auto_now_add=True)
  
# NOTA, si se se hicieron varios cambios y se va a subir a producción, es mas facil
#borrar las migraciones existentes y aplicadas, del VS y de la bd en django_migrations