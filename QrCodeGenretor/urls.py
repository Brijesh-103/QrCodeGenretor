from django.contrib import admin
from django.urls import path
from QrCode import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.generate_qr_code, name='generate_qr_code'),
]
