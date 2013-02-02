import django.shortcuts
from users.models import UserProfile
from flowers.models import Bouquet

def home(request):
    """
    Homepage of the website.
    """
    newcomers = UserProfile.objects.all() # todo: fake implementation!
    bouquets = Bouquet.objects.all() # todo: fake implementation!
    return django.shortcuts.render_to_response('homepage.html', {'new_users': newcomers,
                                                                 'new_bouquets': bouquets})