from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from store.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"), 
    path('catalog/', catalog, name="catalog"),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)