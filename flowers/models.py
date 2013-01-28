from django.db import models

# Create your models here.

class Flower(models.Model):
    """
    A Flower has a name and a graphical representation (which is determined
    from the name.)
    """
    
    # the flowers actually don't have unique names and this property
    # should be replaced by subclassing in some future refactoring
    name = models.CharField(max_length=60)
    bouquet = models.ForeignKey(Bouquet)
    
class Bouquet(models.Model):
    """
    A Bouquet consists of one or more Flowers
    and is given to a particular User.
    A message may be attached.
    """
    
    sender = models.ForeignKey(User)
    receiver = models.ForeignKey(User)
    # dates
    given = models.DateTimeField(default=0)
    accepted = models.DateTimeField(default=0)
    
    # if this is true, accepted is date of rejection;
    # otherwise it's date of acceptance
    rejected = models.BooleanField()
    
    # if this is false, don't expose the sender's identity to the receiver 
    show_sender = models.BooleanField(default=True)
    
    # a short message may be attached:
    message = models.TextField(max_length=512)
    
class User(models.Model):
    """
    A User receives, rejects and owns Bouquets.
    """
    
    name = models.CharField("Your name to be displayed", max_length=128)
    nick = models.CharField("Your nick to log on with", max_length=128)
    avatar = models.ImageField()
    # m or f - the intention behind flowergarden is to give women
    # flowers, but of course nothing will prevent men to receive flowers too.
    # Though, it might be useful sometimes to know the sex of the one you wish
    # to give flowers to...
    sex = models.CharField(max_length=1)