from django.urls import path

from core.views import SecondRoute
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


class CustomSpectacularAPIView(SpectacularAPIView):
    urlconf = 'spectacular_multi_schema.second_urls'


class CustomSpectacularSwaggerView(SpectacularSwaggerView):
    url = 'http://localhost:8000/schema-second'



urlpatterns = [
    path('schema-second', CustomSpectacularAPIView.as_view(), name='schema-second'),
    path('swagger-first', CustomSpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui-first'),
    path('second', SecondRoute.as_view()),

]
