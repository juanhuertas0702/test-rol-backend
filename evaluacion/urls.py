from django.urls import path
from .views import RegistroPostulanteView, LoginView

urlpatterns = [
    # Esta ruta será: /api/postulantes/registro/
    path('registro/', RegistroPostulanteView.as_view(), name='registro_postulante'),
    path('login/', LoginView.as_view(), name='login_postulante'),
]