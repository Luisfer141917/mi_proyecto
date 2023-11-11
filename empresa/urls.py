from django.urls import path
from empresa.views import empresa

urlpatterns = [
    path("",empresa,name="empresa"),
]
