from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Message, Request

@receiver(post_save, sender=Message)
def mark_request_as_responded(sender, instance, created, **kwargs):
    if created:
        request_instance = instance.request
        # Mark the request as responded
        request_instance.is_responded = True
        request_instance.save()

@receiver(post_save, sender=Request)
def delete_old_requests(sender, instance, created, **kwargs):
    if created:
        Request.objects.filter(user_id=instance.user_id).exclude(id=instance.id).delete()