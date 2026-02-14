from rest_framework.views import APIView #Peticiones http
from rest_framework.response import Response
from rest_framework import status

#Importamos el modelo
from posts.models import Post


class PostApiView(APIView):
  # Metodo para obtener los post
  def get(self, request):
    # obtenemos todos los elementos del modelo Post y los guarde en la varibale "posts"
    # posts = Post.objects.all() 
    # objetemos todos los post, hacemos un bucle y por cada post vamos a decirle que guarde el array por cada post
    posts = [post.title for post in Post.objects.all()] 
    # return necesita un response, resonde un status y un contenido data
    return Response(status=status.HTTP_200_OK, data=posts)#
  