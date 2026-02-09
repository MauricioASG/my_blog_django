from django.contrib import admin
from posts.models import Post

# Añadimos decorador
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ['title', 'created_at']
