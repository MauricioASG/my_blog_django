from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

class HelloWorld(View):
  def get(self, request):
    data = {
      'name': 'Mauricio Alejandro Serrano García',
      'years': 23,
      'codes': ['python', 'django', 'react'],
    }
    return render(request, 'hello_world.html', context=data)
# Create your views here.
