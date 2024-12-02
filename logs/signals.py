from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from .models import UserActivityLog

@receiver(user_logged_in)
def log_login(sender, request, user, **kwargs):
    UserActivityLog.objects.create(
        user=user,
        activity="Login berhasil",
        ip_address=get_client_ip(request)
    )

@receiver(user_logged_out)
def log_logout(sender, request, user, **kwargs):
    UserActivityLog.objects.create(
        user=user,
        activity="Logout berhasil",
        ip_address=get_client_ip(request)
    )

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
