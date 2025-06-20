# Django’nun model sınıflarını kullanabilmek için models modülünü içe aktar
from django.db import models

from django.contrib.auth.models import User  # Django'nun standart kullanıcı modeli


# LoginLog adında özel bir model tanımlıyoruz
# Bu model, her kullanıcı girişiyle ilgili log (kayıt) tutacak
class LoginLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    # Hangi kullanıcı giriş yaptı
    ip_address = models.GenericIPAddressField()                 # IP adresi (IPv4 veya IPv6)
    user_agent = models.TextField()                             # Tarayıcı ve cihaz bilgisi
    login_time = models.DateTimeField(auto_now_add=True)        # Giriş zamanı (otomatik)
    is_session_kicked = models.BooleanField(default=False)      # Önceki oturum atıldı mı?

    # Admin panelde nesne göründüğünde nasıl gözükeceğini belirler
    # Örnek: "elifsude - 192.168.0.1 - 2025-06-20 13:24:00"
    def __str__(self):
        return f"{self.user.username} - {self.ip_address} - {self.login_time.strftime('%Y-%m-%d %H:%M:%S')}"

    # Meta → modelin ayarları burada yapılır
    class Meta:
        # Admin panelde görünen isim
        verbose_name = "Login Log"
        verbose_name_plural = "Login Logları"
        # Log kayıtlarını son girişe göre sıralar (en yeni en üstte)
        # ordering = ['-login_time']
