from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'frontend/index.html')


def test(request):
    html = "TEST2"
    return HttpResponse(html)
