from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

def landingPage(request):
    return render(request, 'landingpage/landing_page.html')

class MyLoginView(LoginView):
    template_name = 'landingpage/login.html'
    redirect_authenticated_user = True

class MyLogoutView(LogoutView):
    next_page = '/login/'

my_logout_view = MyLogoutView.as_view()