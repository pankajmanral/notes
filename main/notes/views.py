from django.shortcuts import render,redirect,get_object_or_404
from . models import Note
from django.contrib.auth.decorators import login_required

# Create your views here.

#Read
def note(request):
    data = Note.objects.all()   
    context = {
        'notes' : data 
    }
    return render(request,'notes/notes.html',context)

#Create
@login_required
def addnote(request):
    if request.method == "POST":
        title = request.POST.get('title')
        desc = request.POST.get('desc')

        if title and desc:
            Note.objects.create(title=title, desc=desc)
            return redirect('notes')
    
    return render(request,'notes/addnote.html')

@login_required
# Update
def updatenote(request,id):
    data = get_object_or_404(Note,id=id)
    if request.method == "POST":
        data.title = request.POST.get('title')
        data.desc = request.POST.get('desc')
        data.save()
        return redirect('notes')

    return render(request,'notes/updatenote.html',{'data':data})

@login_required
# Delete 
def deletenote(request,id):
    data = get_object_or_404(Note,id=id)
    if request.method == "POST":
        data.delete()
        return redirect('notes')
    
    context = {
        'data' : data
    }

    return render(request,'notes/deletenote.html',context)