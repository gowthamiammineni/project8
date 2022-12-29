from django.shortcuts import render

# Create your views here.
def second(request):
    d={'favfood':'biryani'}
    return render(request,'second.html',d)
