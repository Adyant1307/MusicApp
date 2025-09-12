from django.conf import settings 
from django.conf.urls.static import static
from . import views
from django.urls import path
urlPattern=[
    path("",views.index,name="indes"),
]