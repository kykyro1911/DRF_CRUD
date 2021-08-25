from django.urls import path
from .api import CRUDCreateApi, CRUDApi, CRUDUpdateApi, CRUDDeleteApi

urlpatterns = [
    path('api',CRUDCreateApi.as_view()),
    path('api/create', CRUDCreateApi.as_view()),
    path('api/<int:pk>',CRUDCreateApi.as_view()),
    path('api/<int:pk>/delete',CRUDCreateApi.as_view()),
]
