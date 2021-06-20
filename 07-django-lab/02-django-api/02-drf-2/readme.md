API view classes 
APIView is the base class. 
GenericAPIView class is the inherited class of APIView class with common mixins.

1. GenericAPIView - in terms of GenericAPIView class we have to use mixins as per our requirements.

2. Permission to authenticated user - we can provide permisson to all the views in the settings.py file or we can provide seperate view permisson in the api.views.py file. 