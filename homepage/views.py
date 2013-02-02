import django.shortcuts
from users.models import UserProfile
from flowers.models import Bouquet

def home(request):
    """
    Homepage of the website.
    """
    
    users_limit = 10
    bouquets_limit = 10
    
    newcomers = UserProfile.objects.all().order_by('user__date_joined').reverse()[:users_limit]
    bouquets = Bouquet.objects.all().order_by('accepted').reverse()[:bouquets_limit]
    
    return django.shortcuts.render_to_response('homepage.html', {'new_users': newcomers,
                                                                 'new_bouquets': bouquets})