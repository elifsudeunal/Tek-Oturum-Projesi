# Django'dan HTML sayfası döndürmek için gerekli fonksiyon
from django.shortcuts import render
# utils.py içindeki "kullanıcıya göre log getiren" fonksiyonu içe aktarıyoruz
from .utils import get_logs_by_user  #  ".utils" = aynı klasördeki utils.py dosyası
from django.contrib.auth.models import User

# Kullanıcının log kayıtlarını görüntüleyen view fonksiyonu
def user_logs_view(request, user_id):
    # ID'si verilen kullanıcıyı veritabanından alıyoruz
    user = User.objects.get(id=user_id)  # get = belirtilen kriterle tek nesne getir

    # Bu kullanıcıya ait tüm log kayıtlarını alıyoruz (utils içindeki fonksiyonla)
    logs = get_logs_by_user(user)

    # logs.html şablon dosyasını kullanarak HTML sayfası oluşturuyoruz
    # {{ logs }} şeklinde verileri template içine aktarıyoruz
    return render(request, 'logs.html', {'logs': logs})
