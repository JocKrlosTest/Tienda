from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import  HomeView, QuejaView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('allauth.urls')),
    path('', HomeView.as_view(),name='home'),
    path('crear_queja/', QuejaView.as_view(),name='crear-queja'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)