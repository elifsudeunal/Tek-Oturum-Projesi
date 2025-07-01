import logging
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from django.contrib.sessions.models import Session
from django.utils.timezone import now
from .models import LoginLog, LogoutLog, FailedLoginLog  # FailedLoginLog'u unutma

logger = logging.getLogger(__name__)

# IP adresini alma fonksiyonu (proxy vs için)
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR')

# Başarılı Giriş Logu
@receiver(user_logged_in)
def on_user_logged_in(sender, request, user, **kwargs):
    if not request.session.session_key:
        request.session.create()

    sessions = Session.objects.filter(expire_date__gte=now())
    for session in sessions:
        data = session.get_decoded()
        user_id = data.get('_auth_user_id')
        if str(user.id) == str(user_id):
            if session.session_key != request.session.session_key:
                try:
                    ip = get_client_ip(request)
                    user_agent = request.META.get('HTTP_USER_AGENT', 'Bilinmiyor')

                    LoginLog.objects.create(
                        user=user,
                        ip_address=ip,
                        user_agent=user_agent,
                        is_session_kicked=True
                    )
                    session.delete()
                    logger.info(f"❌ Eski oturum silindi: {session.session_key}")
                except Exception as e:
                    logger.error(f"Eski oturum log kaydı/silme hatası: {e}")
            else:
                logger.info(f"✅ Şu anki oturum: {session.session_key}")

    try:
        ip = get_client_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', 'Bilinmiyor')

        LoginLog.objects.create(
            user=user,
            ip_address=ip,
            user_agent=user_agent,
            is_session_kicked=False
        )
    except Exception as e:
        logger.error(f"Aktif oturum log kaydı hatası: {e}")

    logger.info(f"👤 {user.username} giriş yaptı. IP: {ip}, UA: {user_agent}")

# Çıkış Logu
@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    try:
        ip = get_client_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', 'Bilinmiyor')

        LogoutLog.objects.create(
            user=user,
            ip_address=ip,
            user_agent=user_agent
        )

        logger.info(f"👋 {user.username} çıkış yaptı. IP: {ip}, UA: {user_agent}")

    except Exception as e:
        logger.error(f"Çıkış log kaydı hatası: {e}")

# Başarısız Giriş Logu (EKLENDİ)
@receiver(user_login_failed)
def log_failed_login(sender, credentials, request, **kwargs):
    username = credentials.get('username', '<unknown>')
    ip = get_client_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT', '')[:500]

    try:
        FailedLoginLog.objects.create(
            username=username,
            ip_address=ip,
            user_agent=user_agent,
            timestamp=now()
        )
        logger.info(f"❌ Başarısız giriş: {username}, IP: {ip}")
    except Exception as e:
        logger.error(f"Başarısız giriş log kaydı hatası: {e}")
