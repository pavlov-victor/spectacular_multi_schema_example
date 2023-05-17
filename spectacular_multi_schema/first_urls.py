from django.urls import path

from core.views import FirstRoute

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


class CustomSpectacularAPIView(SpectacularAPIView):
    urlconf = 'spectacular_multi_schema.first_urls'


class CustomSpectacularSwaggerView(SpectacularSwaggerView):
    url = 'http://localhost:8000/schema-first'


urlpatterns = [
    path('schema-first', CustomSpectacularAPIView.as_view(), name='schema-first'),
    path('swagger-first', CustomSpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui-first'),
    path('first', FirstRoute.as_view()),
]
