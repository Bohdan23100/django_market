import os
from dotenv import load_dotenv

# Завантажуємо змінні з .env
load_dotenv()

# Шлях до кореня проєкту
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 🔐 Секретний ключ (обов’язково змінити в .env)
SECRET_KEY = os.getenv('SECRET_KEY')

# 🔧 Режим налагодження (True тільки для розробки)
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# 🌐 Дозволені хости (додай тут свій домен у продакшені)
ALLOWED_HOSTS = []

# 📦 Установлені додатки
INSTALLED_APPS = [
    # Додай сюди свої додатки
    'social_django',
    'main',
    'user',
    'cart',
    'product',
    'categories',
    'add_product',
    'user_products',

    # стандартні
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

# ⚙️ Мідлвари
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

# 🔀 Основні шляхи
ROOT_URLCONF = 'market.urls'
WSGI_APPLICATION = 'market.wsgi.application'

# 🧠 Шаблони
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # якщо є глобальна папка templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

# 🗄️ База даних
DATABASE_NAME = os.getenv('DATABASE_NAME', 'db.sqlite3')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, DATABASE_NAME),
    }
}

# 🌍 Локаль
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# 📁 Статичні файли
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# 🔐 Google OAuth
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# 🔁 Авторизація
LOGIN_URL = '/auth/login/google-oauth2/'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = '/'  # куди перенаправляти після логіну