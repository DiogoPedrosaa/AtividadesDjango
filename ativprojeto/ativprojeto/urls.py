from django.contrib import admin
from django.urls import path
from promotions import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('promocoes/', views.lista_promocoes, name='lista_promocoes'),
    path('promocoes/<int:promocao_id>/', views.detalhes_promocao, name='detalhes_promocao'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)