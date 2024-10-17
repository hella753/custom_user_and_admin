from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import User
from order.models import UserCart


@receiver(post_save, sender=User)
def create_cart_for_user(sender, **kwargs):
    user_obj = kwargs.get("instance")
    # ორჯერ რომ არ შექმნას სუპერიუზერისთვის კალათა
    # რადგან იუზერმენეჯერი ორჯერ ასეივებს create_userის და create_superuserის დროს
    if not user_obj.is_superuser:
        cart = UserCart(user=user_obj)
        cart.save()
        print(f"cart has been created {cart.id} {user_obj}")