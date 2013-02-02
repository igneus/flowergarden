import django.shortcuts
import django.template
import django.contrib.auth
from django import forms
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
    
    return django.shortcuts.render_to_response('homepage.html',
                                               {'new_users': newcomers, 'new_bouquets': bouquets, 'actor': request.user})

class LoginForm(forms.Form):
    nick = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

def login(request):
    """
    show the login-form
    """
    
    # todo: logged-in user mustn't be abble to log in again without logging out before
    
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if not login_form.is_valid():
            return django.shortcuts.render_to_response('login.html',
                                                       {'form': login_form, 'error_message': 'Login data incomplete.'},
                                                       context_instance=django.template.RequestContext(request))
        nick = login_form.cleaned_data['nick']
        password = login_form.cleaned_data['password']
        user = django.contrib.auth.authenticate(username=nick, password=password)
        if user is None:
            return django.shortcuts.render_to_response('login.html',
                                                        {'form': login_form, 'error_message': 'Log in failed. Wrong nick and/or password.'},
                                                        context_instance=django.template.RequestContext(request))
        if not user.is_active:
            return django.shortcuts.render_to_response('login.html',
                                                        {'form': login_form, 'error_message': 'Log in refused. Your account is disabled.'},
                                                        context_instance=django.template.RequestContext(request))
        django.contrib.auth.login(request, user)
        return django.shortcuts.redirect('homepage.views.home')
    else:
        login_form = LoginForm()
        return django.shortcuts.render_to_response('login.html',
                                                   {'form': login_form},
                                                   context_instance=django.template.RequestContext(request))
    