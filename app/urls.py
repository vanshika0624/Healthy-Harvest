from django.contrib import admin
from django.urls import path
from . import views
app_name='app'

urlpatterns = [
    path('',views.index,name="index"),
    path('predictcrop',views.predictcrop,name="predictcrop"),
    path('videoleaf',views.videoleaf,name="videoleaf"),
]
