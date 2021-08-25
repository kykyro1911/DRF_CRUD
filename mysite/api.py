from rest_framework import generics
from rest_framework.response import Response
from .serializers import CRUDSerializer
from .models import CRUD

class CRUDCreateApi(generics.CreateAPIView):
    queryset = CRUD.objects.all()
    serializer_class = CRUDSerializer

class CRUDApi(generics.ListAPIView):
    queryset = CRUD.objects.all()
    serializer_class = CRUDSerializer

class CRUDUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = CRUD.objects.all()
    serializer_class = CRUDSerializer

class CRUDDeleteApi(generics.DestroyAPIView):
    queryset = CRUD.objects.all()
    serializer_class = CRUDSerializer
