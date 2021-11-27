from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse

# Default view
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def generateUser(request):
    if request.method == 'POST':
        return HttpResponse("POST method used")
    else:
        return render(request, '1.html')