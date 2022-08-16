from django.shortcuts import redirect, render,HttpResponse

# Create your views here.
def home(request):
   return HttpResponse("this is Home")