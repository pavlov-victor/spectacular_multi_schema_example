from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('spectacular_multi_schema.first_urls')),
    path('', include('spectacular_multi_schema.second_urls')),
]
