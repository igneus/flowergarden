import django.shortcuts
from users.models import UserProfile

def home(request):
    """
    Homepage of the website.
    """
    newcomers = UserProfile.objects.all() # todo: fake implementation!
    return django.shortcuts.render_to_response('homepage.html', {'new_users': newcomers})