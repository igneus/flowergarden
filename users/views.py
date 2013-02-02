import django.shortcuts
import django.http
import django.template
import django.contrib.auth.models, django.contrib.auth.hashers
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
        if form.is_valid():
            data = form.cleaned_data
            
            if data['password1'] != data['password2']:
                return django.shortcuts.render_to_response('create_form.html',
                                                   {'form': form, 'error_message': 'The two versions of your password differed!'},
                                                   context_instance=django.template.RequestContext(request))
            
            hashed_password = django.contrib.auth.hashers.make_password(data['password1'])
            user = django.contrib.auth.models.User(username=data['nick'],
                                                   first_name=data['firstname'],
                                                   last_name=data['lastname'],
                                                   email=data['email'],
                                                   password=hashed_password)
            user.save()
            user.userprofile.sex = data['sex']
            user.userprofile.save()
            
            return django.shortcuts.redirect('homepage.views.home') # todo: redirect to the login page
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