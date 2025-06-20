"""
tek_oturum_projesi projesi için WSGI yapılandırması.
 Bu dosya, web sunucularının Django uygulamasını başlatması için gerekli "application" değişkenini sağlar.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

#Django projesini sunucuda yayınlamak (deploy etmek) için kullanılır.
# WSGI = Web Server Gateway Interface → Python uygulamalarıyla web sunucularının konuşmasını sağlar
# (örneğin: Gunicorn, uWSGI vs.).
# Eğer yerel geliştirme (development) yapıyorsan bu dosyayla pek işin olmaz.
# Ama projeyi internette yayınlayacaksan (deploy), bu dosya gereklidir.

import os
# Python'un işletim sistemi (OS) modülünü içe aktarıyoruz.

from django.core.wsgi import get_wsgi_application
# Django'nun wsgi arayüzü fonksiyonunu projeye dahil ediyoruz.
# get_wsgi_application, WSGI uyumlu bir uygulama döner.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tek_oturum_projesi.settings')
# Django'nun hangi ayar dosyasını kullanacağını belirtiyoruz.
# Burada 'tek_oturum_projesi.settings' dosyasını kullan diyoruz. Yani: Ayarları bu dosyadan al.

application = get_wsgi_application()
# WSGI uygulaması oluşturuluyor.
# Sunucu (örneğin Gunicorn), bu 'application' değişkeni üzerinden Django'yu başlatacak.
