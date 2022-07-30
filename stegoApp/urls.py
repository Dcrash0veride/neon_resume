"""gda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.stego, name='stego'),
    path('stego/stegoEncoder.html', views.stegoEncoder, name='stegoEncoder'),
    path('stego/stegoDecoder.html', views.stegoDecoder, name='stegoDecoder'),
    path('stego/<str:pk>/decodesuccess.html', views.decoderSuccess, name='decoderSuccess'),
    path('stego/<str:pk>/', views.stegoSuccessEncoding, name='stegoSuccess'),
#    path('success.html', views.stegoSuccessEncoding, name='success'),
    path('stego/allStego.html', views.allStego, name='allStego'),
    path('stego/download/<str:pk>/', views.downloadStego, name='download'),
]