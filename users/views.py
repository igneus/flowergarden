import django.shortcuts
import django.http
import django.template
import django.contrib.auth.models
from flowers.models import *
from models import UserProfile

def create(request):
    """
    show a form for user registration
    """
    return django.shortcuts.render_to_response('create_form.html', context_instance=django.template.RequestContext(request))

def create_process(request):
    """
    process data from the registration form
    """
    try:
        with_deserved_nick = UserProfile.objects.get(user__username=request.POST['nick'])
    except UserProfile.DoesNotExist:
        # it's OK, the nick is free
        with_deserved_nick = None
    except KeyError:
        return render_to_response('create', {
            'error_message': "You didn't specify a nick.",
        }, context_instance=django.template.RequestContext(request))
    
    if with_deserved_nick:
        return render_to_response('create', {
            'error_message': "Someone already uses the nick '{}'.".format(request.POST['nick']),
        }, context_instance=django.template.RequestContext(request))
    
    
    
    new_user = django.contrib.auth.models.User(username=request.POST['username'],
                                               password=request.POST['password1'])

def list(request):
    """
    list users
    """
    users = UserProfile.objects.all()
    return django.shortcuts.render_to_response('list.html', {'profiles_list': users})

def detail(request, user_id):
    """
    detail of a user
    """
    profile = django.shortcuts.get_object_or_404(UserProfile, pk=user_id)
    bouquets = profile.received_bouquets.all()
        
    return django.shortcuts.render_to_response('detail.html', {'profile': profile, 'bouquets': bouquets})