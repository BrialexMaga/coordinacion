from django.shortcuts import render

def statisticSearchPage(request):
    return render(request, 'studentStatistics/statistics_search_page.html')