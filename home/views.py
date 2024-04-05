from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

# Create your views here.


def index(request):
    return render(request, "frontend/index.html")


@csrf_protect
def test(request):
    return HttpResponse(request.method)
    if request.method == "POST":
        html = "POST"
        return HttpResponse(html)
    else:
        html = "TEST"
        return HttpResponse(html)
