from django.shortcuts import render, redirect, get_object_or_404
from main.models  import Students
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

# Create your views here.

def index(request):
    all_student=Students.objects.all()
    return render(request, 'index.html', {'all_student':all_student})

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method=='POST':
        post = Students()

        if 'name' in request.POST:
            post.name = request.POST['name']
            post.major = request.POST['major']
            post.year = request.POST['year']
            post.classof = request.POST['classof']
            post.average = request.POST['average']

            post.save()

            return redirect('detail', post.id)

def delete(request, student):
    post=get_object_or_404(Students, pk= student)
    post.delete()

    return redirect('index')

def update(request, student):
    post=get_object_or_404(Students, pk= student)

    if request.method=="POST":
        if 'name' in request.POST:
            post.name = request.POST['name']
            post.major = request.POST['major']
            post.year = request.POST['year']
            post.classof = request.POST['classof']
            post.average = request.POST['average']

        post.save()

        return redirect('detail', post.id)
    else:
        return render(request, 'update.html', {'student':post})

def detail(request,student):
    student = get_object_or_404(Students, pk=student)
    return render(request,'detail.html', {'student':student})
