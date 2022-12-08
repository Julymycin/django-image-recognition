from django.db import models

# Create your models here.
class Images(models.Model):
#    file = models.FileField(upload_to='documents/', null=True)
   image = models.ImageField(upload_to='images/', null=True)


from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver

@receiver(pre_delete, sender=Images)
def delete_image_hook(sender, instance, using, **kwargs):
    instance.image.delete()