## Django tarafından otomatik oluşturuldu, sürüm 5.2.3, tarih 19 Haziran 2025

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
# Django'nun veri tabanı işlemleri için gerekli modüller import edildi


# Migration sınıfı, veri tabanında yapılacak değişiklikleri tanımlar
class Migration(migrations.Migration):

    initial = True
    # Bu migration projenin ilk (initial) migration'ıdır.
    # Veri tabanında modelin ilk oluşturulması anlamına gelir.

    # Bu migration, Django'nun kullanıcı modeli (AUTH_USER_MODEL) hazır olmadan çalıştırılamaz
    # yani kullanıcı modeli migration'ına bağlıdır.
    # (swappable_dependency: Değiştirilebilir kullanıcı modeli bağımlılığı)
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginLog',
            # 'LoginLog' adında yeni bir model oluşturulacak

            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                # 'id' alanı: Otomatik artan büyük tam sayı (primary key olarak)

                ('ip_address', models.GenericIPAddressField()),
                # 'ip_address' alanı: IP adresini tutar (IPv4 veya IPv6)

                ('user_agent', models.TextField()),
                # 'user_agent' alanı: Kullanıcının tarayıcı bilgisi (User-Agent string)

                ('login_time', models.DateTimeField(auto_now_add=True)),
                # 'login_time' alanı: Giriş zamanı, kayıt oluşturulunca otomatik atanır

                ('is_session_kicked', models.BooleanField(default=False)),
                # 'is_session_kicked' alanı: Boolean,
                # "oturum sonlandırıldı mı?" bilgisini tutar, varsayılan False

                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                # 'user' alanı: Kullanıcıya (User modeline) bağlı yabancı anahtar (ForeignKey)
                # Kullanıcı silinirse ilişkili login logları da silinir (CASCADE)
            ],
        ),
    ]