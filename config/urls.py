from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from alunos.views import EstadoViewSet

router = DefaultRouter()
router.register(r'estados', EstadoViewSet, basename='estado')

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
