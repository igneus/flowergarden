from django.db import models
import django.db.models.signals
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
    A User receives, rejects and owns Bouquets.
    """
    
    # connection to the User model from django.contrib.auth.models
    user = models.OneToOneField(User)
    
    # todo: prevent users from rewriting each other's avatar by using the same filename
    avatar = models.ImageField(upload_to='avatars')
    # m or f - the intention behind flowergarden is to give women
    # flowers, but of course nothing will prevent men to receive flowers too.
    # Though, it might be useful sometimes to know the sex of the one you wish
    # to give flowers to...
    SEX_CHOICES = (('f', 'female'), ('m', 'male'))
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='f')
    
    def __unicode__(self):
        return "#" + str(self.id) + ": " + self.user.get_full_name() + " (" + self.user.username + ")"
    
    def create_user_profile(sender, instance, created, **kwargs):
        """
        a signal handler (django.contrib.auth.User triggers it on instance creation)
        """
        if created:
            UserProfile.objects.create(user=instance)

    # register signal handler
    django.db.models.signals.post_save.connect(create_user_profile, sender=User)
