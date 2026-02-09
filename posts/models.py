from django.db import models

# creamos una clase para el modelo
class Post(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  created_at = models.DateField(auto_created=True)
  
