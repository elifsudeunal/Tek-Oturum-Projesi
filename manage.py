#!/usr/bin/env python
# Django'nun komut satırı yönetim aracı.
import os # İşletim sistemi ile ilgili fonksiyonları kullanmak için.
import sys # Python çalışma zamanı ortamı ile ilgili fonksiyonlar için (örn: komut satırı argümanları).


def main():
    # main() fonksiyonu: Projenin yönetim işlemlerini başlatan ana fonksiyon.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tek_oturum_projesi.settings')
    # Django'ya hangi ayar dosyasını kullanacağını söyler.
    try:
        from django.core.management import execute_from_command_line
        # Django'nun execute_from_command_line fonksiyonunu içe aktarır.
    except ImportError as exc:
    # Eğer Django yüklü değilse veya bulunamazsa ImportError hatası yakalanır.
        raise ImportError(
            # Django import edilemediğinde kullanıcıya gösterilen hata mesajı.
            "Django import edilemedi. Yüklü olduğundan ve  "
            "PYTHONPATH ortam değişkeninde bulunduğundan emin misiniz? "
            "Sanal ortamı aktif etmeyi unuttunuz mu?"
        ) from exc
    execute_from_command_line(sys.argv)
    # Komut satırından gelen tüm argümanları (sys.argv) Django yönetim fonksiyonuna yollar.


if __name__ == '__main__':
    main()
