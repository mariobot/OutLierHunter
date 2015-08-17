from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'Books/Libros.html')
    
    
def about(request):
    return render(request, 'Books/about.html')

