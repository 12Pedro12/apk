from django.urls import path,include
from rest_framework.routers import DefaultRouter


from .views import RolViewSet, UserViewSet, ClientViewSet, CobradorViewSet,  PrestamoViewSet, CuotaViewSet, PagoViewSet

router = DefaultRouter()
router.register(r'roles', RolViewSet)
router.register(r'users', UserViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'cobrador', CobradorViewSet)
router.register(r'prestamo', PrestamoViewSet)
router.register(r'cuota', CuotaViewSet)
router.register(r'pago', PagoViewSet)
urlpatterns = [
    path('', include(router.urls))
]