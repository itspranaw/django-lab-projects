from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('fourA_app.urls')),
    path('',include('fourB_app.urls')),
]
