from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Note
# Create your views here.


def noteView(request):
    notes=Note.objects.all()
    return render(request,"note.html",{"notes":notes})


def additem(request):
    c=request.POST['content']
    c=Note(content=c)
    c.save()
    return HttpResponseRedirect("/")
def deleteItem(request,id):
    c=Note.objects.get(id=id)
    c.delete()
    return HttpResponseRedirect("/")
