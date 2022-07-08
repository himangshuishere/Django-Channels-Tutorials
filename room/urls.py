from django.urls import path

from room.views import room, rooms

urlpatterns = [
    path('', rooms, name='rooms'),
    path('<slug:slug>/', room, name='room'),
]
