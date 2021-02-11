from django.shortcuts import render

# Create your views here.
def taskList(request):
    return render(request, 'frontend/list.html')