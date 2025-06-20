# Amacı aynı anda birden fazla cihazdan giriş varsa eski oturumu silmek ve
# her girişte giriş bilgilerini LoginLog modeline kaydetmek.

import logging #  Python’un loglama modülü. Bilgilendirme, hata gibi kayıtlar tutmak için.
from django.contrib.auth.signals import user_logged_in # Bu sinyal, biri giriş yapınca otomatik çalışır.
from django.dispatch import receiver # Bu, "bu fonksiyon bir sinyali dinliyor" demek için kullanılır.
from django.contrib.sessions.models import Session # Django’daki tüm oturumları (session) temsil eden model.
from django.utils.timezone import now # Şu anki zamanı (saat + tarih) almak için.
from .models import LoginLog # Aynı klasördeki models.py içinden LoginLog modelini çağırır.

# Bu satır, bu dosyaya özel bir log nesnesi (logger) oluşturur.
logger = logging.getLogger(__name__)
# __name__ → dosyanın adını temsil eder (signals.py içinde çalışıyorsan adı 'users.signals' olur).

# Tarayıcıya özel IP bilgisi varsa al (proxy vs. varsa)
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # Virgülle ayrılmış IP varsa ilkini al, boşluklarını sil.
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    # Eğer özel IP yoksa, normal kullanıcı IP’sini al.
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# Bu fonksiyon, kullanıcı giriş yapınca otomatik çalışır.
@receiver(user_logged_in)
def on_user_logged_in(sender, request, user, **kwargs):
    # Eğer session_key yoksa oluştur
    if not request.session.session_key:
        request.session.create()

    sessions = Session.objects.filter(expire_date__gte=now())
    #  Süresi dolmamış aktif oturumları al.

    # Eski oturumlar için log ve silme
    # Her session’ın içindeki kullanıcı bilgilerini çöz (decode et).
    for session in sessions:
        data = session.get_decoded()
        user_id = data.get('_auth_user_id') # Oturumda saklı olan kullanıcı id’sini al.
        if str(user.id) == str(user_id): # Bu oturum, giriş yapan kullanıcıya ait mi kontrol et.
            if session.session_key != request.session.session_key: # Eğer başka bir cihazdaki oturumsa, sil
                #IP ve tarayıcı bilgilerini al.
                try:
                    ip = get_client_ip(request)
                    user_agent = request.META.get('HTTP_USER_AGENT', 'Bilinmiyor')

                    #LoginLog tablosuna oturum silindi (kicked) olarak kayıt ekle.
                    LoginLog.objects.create(
                        user=user,
                        ip_address=ip,
                        user_agent=user_agent,
                        is_session_kicked=True
                    )
                    session.delete() # Eski oturumu sil.
                    # Konsola bilgi logu yaz: eski oturum silindi.
                    logger.info(f"❌ Eski oturum silindi: {session.session_key}")
                # Bir hata olursa logla.
                except Exception as e:
                    logger.error(f"Eski oturum log kaydı/silme hatası: {e}")
            else: # Bu oturum şu anki oturumsa, sadece bilgi yaz.
                logger.info(f"✅ Şu anki oturum: {session.session_key}")

    # Aktif oturum için log kaydı
    # Giriş yapan kullanıcının bilgilerini al.
    try:
        ip = get_client_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', 'Bilinmiyor')

        # Yeni giriş logunu, normal (kicked değil) olarak kaydet.
        LoginLog.objects.create(
            user=user,
            ip_address=ip,
            user_agent=user_agent,
            is_session_kicked=False
        )
    #Hata olursa logla.
    except Exception as e:
        logger.error(f"Aktif oturum log kaydı hatası: {e}")

    #Kullanıcı adı, IP, tarayıcı bilgisi loga yazılır.
    logger.info(f"👤 {user.username} giriş yaptı. IP: {ip}, UA: {user_agent}")
