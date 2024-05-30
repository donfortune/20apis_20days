from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import Profile
from django.dispatch import receiver
from django.core.mail import send_mail

@receiver(post_save, sender=User)
def createUserProfile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

@receiver(post_save, sender=User)
def saveUserProfile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=User)
def sendEmail(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Our E-commerce Platform!'
        message = f'Hello {instance.username},\n\nWelcome to our platform! We are excited to have you on board.'
        sender_email = 'donfortunet.df@gmail.com'  # Replace with your email
        recipient_email = instance.email
        send_mail(subject, message, sender_email, [recipient_email])