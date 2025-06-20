# "utilities" yani yardımcı işlevler (fonksiyonlar) barındıran bir dosyadır.
# Kod tekrarını önlemek için bazı sık kullanılan sorguları burada tutarız.

# LoginLog modelini aynı klasördeki models.py dosyasından içe aktarıyoruz.
from .models import LoginLog

# Belirli bir kullanıcıya ait tüm giriş loglarını, login_time'a göre sondan başa (yeni -> eski) sıralı olarak getirir.
def get_logs_by_user(user):
    return LoginLog.objects.filter(user=user).order_by('-login_time')

# Verilen tarih aralığında (başlangıç ve bitiş tarihleri dahil) olan giriş loglarını getirir.
def get_logs_by_date_range(start_date, end_date):
    return LoginLog.objects.filter(login_time__gte=start_date, login_time__lte=end_date).order_by('-login_time')
    # login_time >= start_date (gte: "greater than or equal" → büyük veya eşit)
    # login_time <= end_date (lte: "less than or equal" → küçük veya eşit)

# Belirli bir IP adresinden yapılan tüm giriş loglarını, zamana göre azalan sırada getirir.
def get_logs_by_ip(ip_address):
    return LoginLog.objects.filter(ip_address=ip_address).order_by('-login_time')

# Oturumu başka bir cihazdan giriş yapıldığı için sistem tarafından sonlandırılmış (kicked) olan logları getirir.
def get_kicked_sessions():
    return LoginLog.objects.filter(is_session_kicked=True).order_by('-login_time')