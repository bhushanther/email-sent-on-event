
from django.contrib import admin
from django.urls import path,include
import app1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_api/',include('app1.urls')),
]
