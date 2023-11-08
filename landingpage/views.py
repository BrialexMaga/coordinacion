from django.shortcuts import render

def landingPage(request):
    return render(request, 'landingpage/landing_page.html')