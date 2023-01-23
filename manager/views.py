from django.shortcuts import render, redirect
from .models import Soal
from .forms import SoalForm, ContohForm
from django.views.generic.base import View
from django.views.generic import ListView
from django.contrib.auth.models import User
from project.models import UserSubmit

# Create your views here.

class detailJUser(ListView):
    ordering = '-updated'
    model = UserSubmit
    template_name = 'manager/jawaban.html'
    object_list = model.objects.all()

    def get(self,request,*args, **kwargs):
        self.object_list = self.get_queryset().filter(user = kwargs['username'])
        if "search" in request.GET:
            keyword = request.GET['search']
            self.object_list = self.object_list.filter(status__contains = keyword)
        return render(request, self.template_name,{"object_list":self.object_list})

    def post(self, request,*args, **kwargs):
        username = kwargs['username']
        if "accept" in request.POST:
            self.object_list.filter(id = request.POST['accept']).update(
                status = "Solved"
            )
        if "decline" in request.POST:
            self.object_list.get(id = request.POST['decline']).delete()
        return redirect(f'/manager/{username}/')
        

def managerView(request):
    pengguna = User.objects.all()
    jawaban = UserSubmit.objects.all().order_by('-updated')

    context = {
        "pengguna":pengguna,
        "jawaban":jawaban,
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
    contoh = ContohForm()
    context = {
        'form':form
    }

    def get(self, request, *args, **kwargs):
        form = SoalForm(request.POST or None)
        contoh = ContohForm(request.FILES)
        if self.model == "update":
            soal = Soal.objects.get(id = kwargs['id'])
            data = soal.__dict__
            form = SoalForm(request.POST or None, instance=soal, initial=data)
        self.context['form'] = form
        self.context['contoh'] = contoh
        return render(request,'manager/createSoal.html',self.context)

    def post(self,request,*args, **kwargs):
        form = SoalForm(request.POST or None, request.FILES)
        contoh = ContohForm(request.FILES)
        if self.model == "update":
            data = soal.__dict__
            form = SoalForm(request.POST or None, instance=soal, initial=data)
            if form.is_valid():
                form.save()
                return redirect('/manager/')
        self.context['form'] = form
        if form.is_valid():
            if "contoh" in request.FILES:
                Soal.objects.create(
                    title = request.POST['title'],
                    description = request.POST['description'],
                    code = request.POST['code'],
                    category = request.POST['category'],
                    course = request.POST['course'],
                    contoh = request.FILES['contoh'],
                )
            else:
                Soal.objects.create(
                    title = request.POST['title'],
                    description = request.POST['description'],
                    code = request.POST['code'],
                    category = request.POST['category'],
                    course = request.POST['course'],
                )
            return redirect('/manager/')
        return render(request,'manager/createSoal.html',self.context)

def deleteView(request, *args, **kwargs):
    Soal.objects.get(id = kwargs['id']).delete()
    return redirect('/manager/')