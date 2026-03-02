from django.urls import path
from .views import LoginView, AdminView, VerifyTestView, GuardarTestView, EstadisticasView, GenerarDatosView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login_postulante'),
    path('verify-test/', VerifyTestView.as_view(), name='verify_test'),
    path('guardar-test/', GuardarTestView.as_view(), name='guardar_test'),
    path('admin/tests/', AdminView.as_view(), name='admin_tests'),
    path('admin/estadisticas/', EstadisticasView.as_view(), name='admin_estadisticas'),
    path('admin/generar-datos/', GenerarDatosView.as_view(), name='generar_datos'),
]