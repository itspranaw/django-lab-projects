from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('twoA_app.urls')),
    path('',include('twoB_app.urls')),
    path('',include('twoC_app.urls')),
]