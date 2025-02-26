# ...existing code (e.g. INSTALLED_APPS, MIDDLEWARE, DATABASES, etc.)...
# Production settings
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
DEBUG = False
# ...existing code...