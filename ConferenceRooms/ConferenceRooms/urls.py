"""Warsztat3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from conference import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('room/new/', views.AddNewRoom.as_view()),
    path('room/all/', views.ShowRooms.as_view()),
    path('room/delete/<int:id>/', views.DeleteRoom.as_view()),
    path('room/modify/<int:id>/', views.EditRoom.as_view()),
    path('room/reserve/<int:id>/', views.RoomReserve.as_view()),
    path('room/<int:id>/', views.RoomView.as_view() ),
    path('room/search/', views.SearchRoom.as_view()),
    path('table/test/', views.ShowRooms2.as_view())
]
