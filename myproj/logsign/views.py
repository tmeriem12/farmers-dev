from django.shortcuts import render

# Create your views here.
def methodname(request):
    return render(request , "htmlpage.html",{})