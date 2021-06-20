from django.shortcuts import render, HttpResponse

# Create your views here.
from api.hello.add import addition
from api.hello.hell import mul

from .models import sub
def home(request):
    c=addition(5,3)
    m = mul(5,3)
    print(c)
    print(m)
    return HttpResponse("sub value is ")