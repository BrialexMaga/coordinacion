from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

def admin_users(user):
    return user.groups.filter(name='Administradores').exists()

def common_users(user):
    return user.groups.filter(name='Usuarios').exists()

#@user_passes_test(admin_users)
@login_required
def landingPage(request):
    return render(request, 'landingpage/landing_page.html')

class MyLoginView(LoginView):
    template_name = 'landingpage/login.html'
    redirect_authenticated_user = True

class MyLogoutView(LogoutView):
    next_page = '/login/'

my_logout_view = MyLogoutView.as_view()