from django.shortcuts import render, redirect
from .models import Soal
from .forms import SoalForm
from django.views.generic.base import View
from django.views.generic import ListView
from django.contrib.auth.models import User
from project.models import UserSubmit

# Create your views here.

class detailJUser(ListView):
    ordering = 'updated'
    model = UserSubmit
    template_name = 'manager/jawaban.html'
    object_list = model.objects.all()

    def get(self,request,*args, **kwargs):
        self.object_list = self.get_queryset().filter(user = kwargs['username'])
        return render(request, self.template_name,{"object_list":self.object_list})

    def post(self, request,*args, **kwargs):
        if "accept" in request.POST:
            print(request.POST['accept'])
            self.object_list.filter(id = request.POST['accept']).update(
                status = "Solved"
            )
        if "decline" in request.POST:
            print(request.POST['decline'])
            self.object_list.get(id = request.POST['decline']).delete()
        return redirect('/manager/admin/')
        

def managerView(request):
    pengguna = User.objects.all()
    context = {
        "pengguna":pengguna,
    }
    return render(request,'manager/manager.html',context)

def soal(request):
    return render(request,'manager/soal.html')

class SoalListView(ListView):
    model = Soal
    ordering = 'title'
    def get(self,request,*args, **kwargs):
        self.object_list = self.get_queryset()
        if "search" in request.GET:
            self.object_list = self.object_list.filter(title__contains = request.GET['search'])
        return render(request,'manager/soal.html',{"object_list":self.object_list})

class SoalView(View):
    model = None
    form = SoalForm()
    context = {
        'form':form
    }

    def get(self, request, *args, **kwargs):
        form = SoalForm(request.POST or None)
        if self.model == "update":
            soal = Soal.objects.get(id = kwargs['id'])
            data = soal.__dict__
            form = SoalForm(request.POST or None, instance=soal, initial=data)
        self.context['form'] = form
        return render(request,'manager/createSoal.html',self.context)

    def post(self,request,*args, **kwargs):
        form = SoalForm(request.POST or None)
        if self.model == "update":
            soal = Soal.objects.get(id = kwargs['id'])
            data = soal.__dict__
            form = SoalForm(request.POST or None, instance=soal, initial=data)
            if form.is_valid():
                form.save()
                return redirect('/manager/')
        self.context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('/manager/')
        return render(request,'manager/createSoal.html',self.context)

def deleteView(request, *args, **kwargs):
    Soal.objects.get(id = kwargs['id']).delete()
    return redirect('/manager/')