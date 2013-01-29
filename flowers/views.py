# Create your views here.
import django.shortcuts
import django.http
from flowers.models import *

def list(request):
    """
    list users
    """
    users = User.objects.all()
    return django.shortcuts.render_to_response('flowers/list.html', {'users_list': users})

def detail(request, user_id):
    """
    detail of a user
    """
    u = django.shortcuts.get_object_or_404(User, pk=user_id)
    return django.shortcuts.render_to_response('flowers/detail.html', {'user': u})