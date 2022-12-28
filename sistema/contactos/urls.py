from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edad/<int:edad>', views.edad_verificacion, name='edad')
]


