from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.db.models.signals import pre_save, post_save

from .utils import unique_slug_generator


User = settings.AUTH_USER_MODEL

class RegisterForm(models.Model):
    full_Name       = models.CharField(max_length=120)
    email           = models.CharField(max_length=120, null=True, blank=True)
    phone_Number    = models.CharField(max_length=10, null=True, blank=True)
    question        = models.CharField(max_length=360, null=True, blank=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    #my_date_field   = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.full_Name

    @property
    def title(self):
        return self.full_Name

# def rl_pre_save_receiver(sender, instance, *args, **kwargs):
#     instance.category = instance.category.capitalize()
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#
# pre_save.connect(rl_pre_save_receiver, sender=RegisterForm)
