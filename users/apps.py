# Bu dosya, Django’ya “bu uygulama nasıl yapılandırılmalı” onu söyler.
# Uygulamanın adı burada: users

from django.apps import AppConfig
# Django'nun uygulama yapılandırma sınıfını içe aktarıyoruz
# Bu sınıfı kullanarak uygulamaya özel ayarlar yapabiliriz

#UsersConfig adında bir yapılandırma sınıfı oluşturuyoruz.
# Bu sınıf, users adlı uygulamamızın ayarlarını temsil eder.
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    #  Modellerde otomatik oluşturulan id alanları için varsayılan alan türünü belirliyoruz.
    name = 'users'
    # Bu yapılandırma hangi uygulamaya ait?
    # users uygulamasına ait olduğunu belirtiyoruz.

    # ready() metodu, uygulama başlarken çalışan özel bir fonksiyondur.
    # Uygulama yüklendiğinde çalıştırılacak şeyleri buraya yazarsın.
    def ready(self):
        import users.signals  # signals.py dosyasını yüklüyoruz
        # Bu sayede, sinyal tanımları aktif hale gelir.
