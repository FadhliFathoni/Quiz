from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.views.generic import ListView
from manager.models import Soal
from .models import UserSubmit
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def SoalListView(request):
    object_list = Soal.objects.all()
    return render(request,'landingPage.html',{"object_list":object_list})

def loginView(request):
    if User.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        uname = request.POST['username']
        pw = request.POST['password']
        akun = authenticate(username = uname, pasword = pw)
        if akun is not None:
            login(request, akun)
            return redirect('/')
    return render(request,'login.html')

class CourseListView(ListView):
    model = Soal
    template_name = 'course.html'

    def get(self,request,*args, **kwargs):
        self.object_list = self.get_queryset().filter(course = kwargs['course'])
        if "id" in kwargs:
            self.object_list = self.object_list.filter(id = kwargs['id'])
        return render(request,self.template_name,{"object_list":self.object_list})