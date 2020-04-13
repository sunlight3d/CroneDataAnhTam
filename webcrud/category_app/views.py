from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    dict_person = {"name": "Hoang"}
    return render(request, 'category_app/index.html', context=dict_person)