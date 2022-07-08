
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('core.urls'), name='core_urls'),
    path('rooms/', include('room.urls'), name='room_urls'),
    path('admin/', admin.site.urls),
]
