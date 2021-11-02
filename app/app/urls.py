"""App urls configurations."""
from django.contrib import admin
from django.urls import include, path
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include('cookery.urls', namespace='cookery')),
]
