from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre_nos, name='sobre_nos'),
    path('artigo/<int:id>/', views.artigo_detalhe, name='detalhe_artigo'),
    path('contato/', views.fale_conosco, name='fale_conosco'),

    path('admin/', admin.site.urls),

    path('api/token/', TokenObtainPairView(), nam='token_obtain_pair'),

    path('api/token/refresh/', TokenObtainPairView(), nam='token_obtain_pair'),

    path('api/artigos/', views.api_listar_artigos, name='api_artigos'),    
    path('api/artigo/novo/', views.api_criar_artigo),
]