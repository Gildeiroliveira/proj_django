from django.contrib import admin
from django.urls import path, include
from amz import views


urlpatterns = [
    #rota , views responsavel , nome de referencia
    path("admin/", admin.site.urls),
    path('hello', views.hello, name='hello'),
    path('', views.amz, name='home'),
    path('cadastro/', views.cadastro, name='Itens')
    
]


