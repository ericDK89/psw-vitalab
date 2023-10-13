from django.urls import path
from . import views
from usuarios import views as usuarios_views

urlpatterns = [
    path('solicitar_exames/', views.solicitar_exames, name='solicitar_exames'),
    path('usuarios/login/', usuarios_views.login, name='login')
]
