from django.conf import settings            # when in local host (not in vercel)
from django.conf.urls.static import static  # when in local host (not in vercel)

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include('core.urls')),  
    path("items/", include('item.urls')), # vai buscar no app 'item' no arquivo 'urls.py' 
    path("dashboard/", include('dashboard.urls')),
    path("inbox/", include('conversation.urls')),
    path("admin/", admin.site.urls),
] 


if not settings.USE_VERCEL:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)    