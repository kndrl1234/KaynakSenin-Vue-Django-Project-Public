from django.contrib import admin
from django.urls import path, include
from django.conf import settings ## ADDED
from django.conf.urls.static import static ## ADDED

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('KaynakApp.API.urls')),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)