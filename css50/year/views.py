from django.shortcuts import render
import datetime

# Create your views here.
def newyear(request):
    current = datetime.datetime.now()

    return render(request, "newyear/year.html",{
        "newyear":current.month == 1 and current.day == 1
    })