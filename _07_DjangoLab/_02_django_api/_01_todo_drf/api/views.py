from django.shortcuts import render
from django.http import JsonResponse

#working with functional views
from rest_framework.decorators import api_view #to work with drf api view
from rest_framework.response import Response 

from .models import Task

#importing serializers
from .serializers import TaskSearializer

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    # return JsonResponse("API Base Point", safe=False)

    #django restframework response
    api_urls = {
        'list': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    #fetching data from database
    tasks = Task.objects.all().order_by('-id')

    #serializing the data (many=True, as we are serializing loads of data)
    serializer = TaskSearializer(tasks, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSearializer(task, many=False) #as we are fetching specific single task with their id
    return Response(serializer.data)

#create 
@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSearializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

#update
@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSearializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)



#delete
@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    
    return Response("Task successfully deleted")

