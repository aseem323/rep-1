from django.urls import path, include
from application.views import test,function1
urlpatterns = [
path("",test),
path("home",function1),
    
]
  