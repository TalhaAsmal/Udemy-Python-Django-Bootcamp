from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<em>Second App</em>")

def help(request):
    my_dict = {'insert_me': '<h1>Help Page</h1>'}
    return render(request, 'AppTwo/help.html', context=my_dict)
