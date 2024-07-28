
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('blog.urls')),
    path('summernote/', include('django_summernote.urls')),
    # path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#colocando o do blog

if settings.DEBUG:
     urlpatterns += static(
         settings.MEDIA_URL, 
         document_root=settings.MEDIA_ROOT)
