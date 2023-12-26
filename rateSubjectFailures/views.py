from django.shortcuts import render

def filterRateSubjectFailures(request):

    return render(request, 'rateSubjectFailures/failing_rate_filter.html')