from django.contrib import admin
from django.urls import path

from droplet.views import drop, lift

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drop', drop, name='droplet'),
    path('_/<slug:file_hash>', lift, name='lift')
]
