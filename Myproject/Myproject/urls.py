
from django.contrib import admin
from django.urls import path,include
#swagger config
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
#jwt view
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

#swagger views settings

schema_view = get_schema_view(
    openapi.Info(
        title="Swagger with django API",
        default_version='v1',
        description="powered by spaceyatech and Tamarcom Technology",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@expense.local"),
        license=openapi.License(name="Test License")),
        public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('admin/', admin.site.urls),
    #add Myapp urls here
    path('', include("Myapp.urls")),
    # for swagger ui
    path ('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path ('api/api.json', schema_view.without_ui( cache_timeout=0), name='schema-swagger-ui'),
    path ('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]