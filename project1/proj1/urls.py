from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('oneC_app.urls')),
    path('',include('oneD_app.urls')),
]
