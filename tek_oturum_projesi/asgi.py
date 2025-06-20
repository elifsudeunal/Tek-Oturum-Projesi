# ASGI, Django'nun modern asenkron sunucu-gateway arayüzüdür
# (Asynchronous Server Gateway Interface).

import os
# Sistem ortam değişkenlerini ayarlamak için kullanılır.

from django.core.asgi import get_asgi_application
# Django’dan get_asgi_application fonksiyonunu getirir.
# Bu fonksiyon, Django uygulamasını ASGI uygulaması olarak çalıştırmak için gerekli callable objeyi döner.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tek_oturum_projesi.settings')
# Bu değişken Django'nun hangi ayar dosyasını (settings.py) kullanacağını belirtir.

application = get_asgi_application()
# Bu, ASGI sunucusunun kullanacağı callable objedir (giriş noktası).
# Sunucu, bu application objesini kullanarak Django uygulamanıza istekleri iletecek.
