# Django'da admin.py, admin panelini özelleştirmek için kullanılır.
# Admin panelde hangi modellerin görüneceğini, hangi alanların listeleneceğini, filtreleneceğini ve aranacağını burada tanımlarsın.
# Yani, admin.py projenin yönetim arayüzünü düzenler.

from django.contrib import admin
# Django'nun admin modülünü projeye dahil ediyoruz.
from .models import LoginLog
# Aynı klasördeki models.py dosyasından LoginLog modelini alıyoruz.
# Bu model, giriş kayıtlarını tutuyor.
from django.contrib.sessions.models import Session
# Django'nun oturum (session) modeli.

# LoginLog modelini admin paneline kaydeder.
# Bu dekoratör sayesinde model admin panelde görünür.
@admin.register(LoginLog)
# Admin panelde LoginLog modelinin nasıl görüneceğini ayarlayan sınıf.
# admin.ModelAdmin sınıfını miras alarak özelleştirme yapıyoruz.
class LoginLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'ip_address', 'user_agent', 'login_time', 'is_session_kicked')
    # Admin panelde LoginLog listesi görüntülenirken gösterilecek sütunlar.
    # user: kullanıcı adı
    # ip_address: giriş yapılan IP adresi
    # user_agent: cihaz/ tarayıcı bilgisi
    # login_time: giriş zamanı
    # is_session_kicked: oturumun kapatılıp kapatılmadığı (boolean)
    list_filter = ('user', 'login_time', 'ip_address', 'is_session_kicked')
    # Admin panelin sağ tarafında filtre seçenekleri çıkar.
    # Kullanıcı, giriş zamanı, IP adresi ve oturum kapatma durumuna göre filtreleme yapabilirsin.
    search_fields = ('user__username', 'ip_address', 'user_agent')
    # Admin panelde üstte arama çubuğu olur.
    # Buraya yazdığında 'user'un kullanıcı adı, IP veya cihaz bilgisi içinde arama yapar.
    # 'user__username' ifadesi: LoginLog modeli 'user' ile User modeline bağlı,
    # oradaki 'username' alanında arama yap demek.

