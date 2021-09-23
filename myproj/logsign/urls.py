from django.urls import path
from . import views
urlpatterns = [
   path('',views.methodname,name="methodname"),
]
