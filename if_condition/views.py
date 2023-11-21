from django.shortcuts import render

# Create your views here.
def if_cond(request):
    d={'a':20,'b':30,'c':40}
    return render(request,'greater.html',d)
