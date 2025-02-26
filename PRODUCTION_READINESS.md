# Production Readiness Checklist

- [x] Dashboard view passes required context (projects and current_project).
- [x] DEBUG is set to False.
- [x] ALLOWED_HOSTS is properly configured.
- [ ] Enforce HTTPS (e.g. SECURE_SSL_REDIRECT, secure cookies).
- [ ] Configure proper logging and error monitoring.
- [ ] Use a robust WSGI server (e.g. Gunicorn) and configure static files.
- [ ] Review security settings (e.g. HSTS, CSRF, and XSS protections).
