from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
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
    def form_invalid(self, form):
        messages.error(self.request, 'Credenciales incorrectas. Inténtalo de nuevo.')
        return super().form_invalid(form)
    
    template_name = 'landingpage/login.html'
    redirect_authenticated_user = True

class MyLogoutView(LogoutView):
    next_page = '/login/'

my_logout_view = MyLogoutView.as_view()