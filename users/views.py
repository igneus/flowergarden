import django.shortcuts
import django.http
import django.template
import django.contrib.auth.models
from flowers.models import *
from models import UserProfile
from forms import CreateUserForm

def create(request):
    """
    show a form for user registration
    """
    if request.method == 'POST':
        # arriving data to process
        form = CreateUserForm(request.POST)
        if form.is_valid:
            # todo: process data, create a user account, redirect to the login page
            pass;
        else:
            return django.shortcuts.render_to_response('create_form.html',
                                                   {'form': form, 'error_message': 'Input invalid.'},
                                                   context_instance=django.template.RequestContext(request))
    else:
        # show an empty form 
        form = CreateUserForm()
        return django.shortcuts.render_to_response('create_form.html',
                                                   {'form': form},
                                                   context_instance=django.template.RequestContext(request))

def create_process(request):
    """
    process data from the registration form
    """
    pass

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