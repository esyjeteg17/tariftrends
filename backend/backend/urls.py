"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from tariffs.views import TariffsAPIView, ModemTariffAPIView, HomephoneTariffAPIView, TVTariffAPIView, \
    InternetTariffAPIView, SmartTariffAPIView, RegisterView, UserDetailView, UpdateFavoriteAPIView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('api/user/', UserDetailView.as_view(), name='user-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('admin/', admin.site.urls),
    path('api/v1/mobile/<int:pk>/favorite/', UpdateFavoriteAPIView.as_view(), name='update-favorite'),
    path('api/v1/mobile/', TariffsAPIView.as_view()),
    path('api/v1/modems/', ModemTariffAPIView.as_view()),
    path('api/v1/homephone/', HomephoneTariffAPIView.as_view()),
    path('api/v1/tv/', TVTariffAPIView.as_view()),
    path('api/v1/internet/', InternetTariffAPIView.as_view()),
    path('api/v1/smart/', SmartTariffAPIView.as_view()),
]
