from django.shortcuts import render

def searchPage(request):
    return render(request, 'studenthistory/search_page.html')

def showHistory(request):
    return render(request, 'studenthistory/show_history.html')