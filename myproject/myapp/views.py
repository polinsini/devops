# In <app_name>/views.py
from .models import MyModel  # Импорт MyModel
from django.http import HttpResponse  # Импортируем HttpResponse

def index(request):
    return HttpResponse("Welcome to My App!")