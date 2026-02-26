from django.urls import path
from .views import LoginView, AdminView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login_postulante'),
    path('admin/tests/', AdminView.as_view(), name='admin_tests'),
]