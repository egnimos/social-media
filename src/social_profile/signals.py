from django.db.models.signals import post_save
from .models import SocialProfile, Relationship, STATUS_CHOICES
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
    print('sender', sender)
    print('instance', instance)

    # if the new user is created then create a social profile 
    if created:
        SocialProfile.objects.create(user=instance)

@receiver(post_save, sender=Relationship)
def post_save_add_to_friend(sender, instance, created, **kwargs):
    sender_ = instance.sender
    receiver_ = instance.receiver
    # if status is accepted
    if instance.status == STATUS_CHOICES[-1][0]:
        # add receiver in a senders friend list
        sender_.friends.add(receiver_.user)
        sender_.save()
         # add sender in a receiver friend list
        receiver_.friends.add(sender_.user)
        receiver_.save()

