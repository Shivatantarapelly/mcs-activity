from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver


@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print("-----------------------")
    print("Logged in signal...  run intro...")
    print("sender", sender)
    print("request", request)
    print("user", user)
    print("user password", user.password)
    print(f'kwargs: {kwargs}')

# user_logged_in.connect(login_success, sender=User)
