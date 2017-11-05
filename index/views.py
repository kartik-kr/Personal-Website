from django.http import HttpResponse
from django.http import FileResponse, Http404
from django.template import loader
from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import ContactMe
from django.core.exceptions import ViewDoesNotExist

class IndexView(generic.ListView):
        template_name = 'home/index.html'
        def get_queryset(self):
                all_Contacts = ContactMe.objects.all()


# def index(request):
#       all_Contacts = ContactMe.objects.all()
#       context = {'all_Contacts' : all_Contacts}
# return render(request,'home/index.html',context,)

def Blogs(request, input_id):
        return HttpResponse("<h4> Kartik K R is cooking his Blog!!   See you again!<h4>")

def message(request):
        all_Contacts = ContactMe.objects.all()
        try:
                new_message = ContactMe()
                new_message.name = request.POST['name']
                new_message.mail = request.POST['email']
                new_message.mobile = request.POST['mobile']
                new_message.message = request.POST['message']
                new_message.save()
        except Error:
                raise Http404("The Journey of Life is filled with Disappointments this is one of them")
        else:
                return render(request,'home/detail.html', {'ContactMe': all_Contacts})

def Error(request):
        return render(request,'home/error.html')