from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Giriş Logu
class LoginLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)              # Giriş yapan kullanıcı
    login_time = models.DateTimeField(auto_now_add=True)                  # Giriş zamanı
    logout_time = models.DateTimeField(null=True, blank=True)             # Çıkış zamanı
    ip_address = models.GenericIPAddressField(null=True, blank=True)      # IP adresi
    user_agent = models.TextField(null=True, blank=True)                  # Tarayıcı bilgisi
    is_session_kicked = models.BooleanField(default=False)                # Önceki oturum atıldı mı?
    session_key = models.CharField(max_length=40, null=True, blank=True) # Oturum anahtarı

    def session_duration(self):
        if self.logout_time:
            return self.logout_time - self.login_time
        return None

    def __str__(self):
        return f"{self.user.username} - {self.login_time.strftime('%Y-%m-%d %H:%M:%S')}"

    class Meta:
        verbose_name = "Login Log"
        verbose_name_plural = "Login Logları"
        ordering = ['-login_time']


# Çıkış Logu
class LogoutLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    logout_time = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} çıkış yaptı ({self.logout_time.strftime('%Y-%m-%d %H:%M:%S')})"

    class Meta:
        verbose_name = "Logout Log"
        verbose_name_plural = "Logout Logları"
        ordering = ['-logout_time']


# Başarısız Giriş Logu
class FailedLoginLog(models.Model):
    username = models.CharField(max_length=150)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} (Başarısız Giriş)"

    class Meta:
        verbose_name = "Başarısız Giriş Logu"
        verbose_name_plural = "Başarısız Giriş Logları"
        ordering = ['-timestamp']
