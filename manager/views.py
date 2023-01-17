from django.shortcuts import render, redirect
from .models import Soal
from .forms import SoalForm
from django.views.generic.base import View
from django.views.generic import ListView

# Create your views here.

def soal(request):
    return render(request,'manager/soal.html')

class SoalListView(ListView):
    model = Soal
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