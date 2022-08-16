from django.shortcuts import redirect, render,HttpResponse

# Create your views here.
def events(request):
   return HttpResponse("this is events page")
