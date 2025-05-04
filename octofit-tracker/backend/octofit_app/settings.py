# Adicionar o aplicativo 'octofit' à lista de INSTALLED_APPS

try:
    INSTALLED_APPS
except NameError:
    INSTALLED_APPS = []

INSTALLED_APPS += [
    'octofit',
    'rest_framework',
    'corsheaders',
]
INSTALLED_APPS.extend([
    'octofit',
    'rest_framework',
    'corsheaders',
])

INSTALLED_APPS += [
    'octofit_app',
]

INSTALLED_APPS = list(set(INSTALLED_APPS))

# Configurar middleware para CORS
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

# Configurar CORS para permitir todas as origens
CORS_ALLOW_ALL_ORIGINS = True

# Add MongoDB database connection
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'HOST': 'localhost',
        'PORT': 27017,  # Corrigido para ser um número inteiro
    }
}

# Enable CORS to allow all origins, methods, and headers
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]
CORS_ALLOW_HEADERS = [
    'content-type',
    'authorization',
    'x-csrftoken',
]

# Allow all hosts
ALLOWED_HOSTS = ['*']