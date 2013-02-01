from django.db import models
from users.models import UserProfile
    
class Bouquet(models.Model):
    """
    A Bouquet consists of one or more Flowers
    and is given to a particular User.
    A message may be attached.
    """
    
    sender = models.ForeignKey(UserProfile, related_name='sent_bouquets')
    receiver = models.ForeignKey(UserProfile, related_name='received_bouquets')
    # dates
    given = models.DateTimeField(default=0)
    accepted = models.DateTimeField(default=0, blank=True, null=True)
    
    # if this is true, accepted is date of rejection;
    # otherwise it's date of acceptance
    rejected = models.BooleanField(default=False)
    
    # if this is false, don't expose the sender's identity to the receiver 
    show_sender = models.BooleanField(default=True)
    
    # a short message may be attached:
    message = models.TextField(max_length=512)
    
    def __unicode__(self):
        return "#" + str(self.id) + " for " + self.receiver.user.username
    
    
class FlowerType(models.Model):
    """
    A type of Flowers available for your Bouquets.
    """
    name = models.CharField(max_length=64)
    pretty_name = models.CharField(max_length=64)
    
    def __unicode__(self):
        return self.pretty_name
    
    # todo: not all flower types should be available to everyone at every time - the less common ones should be somehow rare or expensive    

class Flower(models.Model):
    """
    A particular Flower contained in a particular Bouquet.
    """
    
    # the flowers actually don't have unique names and this property
    # should be replaced by subclassing in some future refactoring
    bouquet = models.ForeignKey(Bouquet)
    flower_type = models.ForeignKey(FlowerType)
    position = models.IntegerField(help_text="Position of the flower in a bouquet (beginning with 0)")
    
    def __unicode__(self):
        return "#" + str(self.id) + ": " + self.flower_type.pretty_name + " in bouquet #" + str(self.bouquet.id)
