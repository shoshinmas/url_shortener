from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('url/index.html', c)