"""
tek_oturum_projesi projesinin URL ayarlarıdır.

`urlpatterns` listesi, URL'leri view'lara (sayfalara) yönlendirir.
For more information please see:    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

# Bu dosya, projenin en üst seviyedeki URL yönlendirici (router) dosyasıdır.
# Yani tarayıcıdan gelen istekleri hangi view’lere (sayfalara) yönlendireceğini belirler.

from django.contrib import admin
# Django’nun hazır gelen admin panel modülünü import ediyoruz.
from django.urls import path
# path() fonksiyonunu getiriyor.
# Bu fonksiyon, hangi URL’ye hangi sayfa (view) gösterilecek bunu tanımlar.

# Bu liste Django’ya “şu URL gelirse şuraya gönder” talimatı verir
urlpatterns = [
    path('admin/', admin.site.urls),
    # Yani: http://localhost:8000/admin/ → Admin paneline gider.
]
