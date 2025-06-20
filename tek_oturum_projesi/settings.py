"""
For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
# Dosya ve klasör yollarını platformdan bağımsız tanımlamak için.

# BASE_DIR, projenin ana klasörünü temsil eder (yani en dış klasör).
# Diğer yollar buna göre tanımlanır.
BASE_DIR = Path(__file__).resolve().parent.parent


# Geliştirme için hızlı ayarlar. Gerçek sunucuda (production) bu ayarlarla çalıştırılmaz.
# Gizli bilgiler, güvenlik ayarları bu bölümde dikkatli kullanılmalı.

# Django'nun gizli anahtarı. Üretimde kimseyle paylaşılmamalı.
SECRET_KEY = 'django-insecure-_v%t$tnt7k=-)ejz6cejc+3751ej2_t0n#h4luze_ujxk8lr_i'

# DEBUG = True ise hata detayları ekranda görünür. Gerçek sunucuda mutlaka False yapılmalı.
DEBUG = True

# Bu sunucuya hangi adreslerden istek kabul edilecek?
# Geliştirmede boş bırakılabilir.
ALLOWED_HOSTS = []


# Application definition
# Django'nun kendi uygulamaları + bizim yazdığımız uygulamalar (örnek: users)

INSTALLED_APPS = [
    'django.contrib.admin',             # Admin paneli
    'django.contrib.auth',              # Kullanıcı yönetimi (giriş, şifre)
    'django.contrib.contenttypes',      # Model sistemi için gerekli
    'django.contrib.sessions',          # Oturum (session) yönetimi
    'django.contrib.messages',          # Uyarılar / mesajlar
    'django.contrib.staticfiles',       # CSS, JS gibi statik dosyalar

    'users.apps.UsersConfig',           # Kendi oluşturduğum "users" uygulaması
    # Eğer sadece 'users' yazarsan da çoğu zaman çalışır ama apps.py’de tanımlı özel ayarlar devreye girmez.
]

# Django'nun isteği nasıl işleyeceğini belirleyen ara katmanlar
# Güvenlik, oturum gibi işlemleri takip eder.

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',              # Güvenlik için
    'django.contrib.sessions.middleware.SessionMiddleware',       # Oturum yönetimi
    'django.middleware.common.CommonMiddleware',                  # Genel ayarlar
    'django.middleware.csrf.CsrfViewMiddleware',                  # Form güvenliği
    'django.contrib.auth.middleware.AuthenticationMiddleware',    # Giriş kontrolü
    'django.contrib.messages.middleware.MessageMiddleware',       # Uyarı mesajları
    'django.middleware.clickjacking.XFrameOptionsMiddleware',     # Tıklama dolandırıcılığına karşı koruma
]

# Ana URL dosyasının ismi. (urls.py bu dosyada bulunuyor)
ROOT_URLCONF = 'tek_oturum_projesi.urls'

# Şablon (HTML) sisteminin ayarları.
# HTML dosyalarının nasıl kullanılacağını belirtir.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Django'nun kendi şablon sistemi
        'DIRS': [],                       # HTML dosyalarının bulunduğu özel klasör (şu an boş)
        'APP_DIRS': True,                 # Her uygulama içindeki templates klasörünü otomatik bul
        'OPTIONS': {
            'context_processors': [       # HTML dosyalarına bazı değişkenleri otomatik gönder
                'django.template.context_processors.request',           # HTML şablonlara request (HTTP isteği) nesnesini ekler.
                'django.contrib.auth.context_processors.auth',          # user nesnesini şablonlara otomatik ekler.
                'django.contrib.messages.context_processors.messages',  # Django mesaj sistemini şablonlarda kullanmanı sağlar.
                # (örnek: “başarıyla giriş yaptınız” mesajı).
            ],
        },
    },
]


# WSGI, sunucularla Django’yu çalıştırmak için kullanılan arabirim (web sunucu bağlantısı).
WSGI_APPLICATION = 'tek_oturum_projesi.wsgi.application'

# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# Veritabanı ayarları. Şu an SQLite kullanılıyor (geliştirme için yeterli).
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',          # Veritabanı motoru: SQLite
        'NAME': BASE_DIR / 'db.sqlite3',                 # Veritabanı dosyasının yolu
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

# Şifre doğrulama kuralları.Kullanıcının şifresi güçlü mü diye kontrol eder.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },  # Kullanıcı adı gibi kolay şifreleri engeller
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },  # Minimum uzunluk kontrolü
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },  # "123456" gibi yaygın şifreleri engeller
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },  # Tamamen sayılardan oluşan şifreleri engeller
]



# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

# Dil ve zaman ayarları
LANGUAGE_CODE = 'tr'             # Arayüz dili (İngilizce - ABD)
TIME_ZONE = 'Europe/Istanbul'       # Saat dilimi

USE_I18N = True             # Uluslararasılaştırma desteği (çok dil desteği)
USE_L10N = True             # Yerelleştirme (tarih-saat, sayı formatları) aktif olur
USE_TZ = True               # Zaman dilimi kullanılsın mı?




# https://docs.djangoproject.com/en/5.2/howto/static-files/

# Statik dosyaların yolu (CSS, JS vs.)
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

# Varsayılan olarak her modeldeki id alanı için BigAutoField kullanılır.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Basit log sistemi.
# Konsola bilgi mesajları (INFO) yazdırır.
LOGGING = {
    'version': 1,                           # Log sistemi versiyonu (hep 1 kalır)
    'disable_existing_loggers': False,      # Var olan logger'lar kapatılmasın
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',  # Konsola yazdır
        },
    },
    'root': {
        'handlers': ['console'],       # Root logger konsola yazsın
        'level': 'INFO',               # En düşük gösterilecek seviye: INFO
    },
}