from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registerapi/', include('registerapi.urls')),
    path('Hvregistration/', include('Hvregistration.urls')),
    path('Doregistration/', include('Doregistration.urls')),
    path('scregistration/', include('scregistration.urls')),
    path('lobourconregistration/', include('lobourconregistration.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

