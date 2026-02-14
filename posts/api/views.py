from rest_framework.views import APIView #Peticiones http
from rest_framework.response import Response
from rest_framework import status


class PostApiView(APIView):
  # Metodo para obtener los post
  def get(self, request):
    # return necesita un response, resonde un status y un contenido data
    return Response(status=status.HTTP_200_OK, data='Hola mundo')#
  