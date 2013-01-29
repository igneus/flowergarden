from django.db import models

# todo: the users should be in their own package
    
class User(models.Model):
    """
    A User receives, rejects and owns Bouquets.
    """
    
    name = models.CharField("Your name to be displayed", max_length=128)
    nick = models.CharField("Your nick to log on with", max_length=128) # todo: nick *must* be unique
    avatar = models.ImageField(upload_to='avatars')
    # m or f - the intention behind flowergarden is to give women
    # flowers, but of course nothing will prevent men to receive flowers too.
    # Though, it might be useful sometimes to know the sex of the one you wish
    # to give flowers to...
    sex = models.CharField(max_length=1)
    
    def __unicode__(self):
        return "#" + str(self.id) + ": " + self.name + " (" + self.nick + ")"
    
    
class Bouquet(models.Model):
    """
    A Bouquet consists of one or more Flowers
    and is given to a particular User.
    A message may be attached.
    """
    
    sender = models.ForeignKey(User, related_name='sent_bouquets')
    receiver = models.ForeignKey(User, related_name='received_bouquets')
    # dates
    given = models.DateTimeField(default=0)
    accepted = models.DateTimeField(default=0) # todo: allow empty
    
    # if this is true, accepted is date of rejection;
    # otherwise it's date of acceptance
    rejected = models.BooleanField(default=False)
    
    # if this is false, don't expose the sender's identity to the receiver 
    show_sender = models.BooleanField(default=True)
    
    # a short message may be attached:
    message = models.TextField(max_length=512)
    
    def __unicode__(self):
        return "#" + str(self.id) + " for " + self.receiver.nick
    
    
class Flower(models.Model):
    """
    A Flower has a name and a graphical representation (which is determined
    from the name.)
    """
    
    # the flowers actually don't have unique names and this property
    # should be replaced by subclassing in some future refactoring
    name = models.CharField(max_length=60)
    bouquet = models.ForeignKey(Bouquet)
    
    def __unicode__(self):
        return "#" + str(self.id) + ": " + self.name
