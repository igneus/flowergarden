# Create your views here.
import django.shortcuts
import django.http
from flowers.models import *

def list(request):
    """
    list users
    """
    users = UserProfile.objects.all()
    return django.shortcuts.render_to_response('flowers/list.html', {'profiles_list': users})

def detail(request, user_id):
    """
    detail of a user
    """
    p = django.shortcuts.get_object_or_404(UserProfile, pk=user_id)
    return django.shortcuts.render_to_response('flowers/detail.html', {'profile': p})