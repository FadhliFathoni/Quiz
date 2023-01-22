from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate, logout
from django.views.generic.base import View
from django.views.generic import ListView
from manager.models import Soal
from .models import UserSubmit
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

# @login_required(login_url='/login/')

class SoalListView(TemplateView):
    template_name = 'landingPage.html'
    course = [
        {"course":"Java","img":"img/java.jpg"},
        {"course":"PHP","img":"img/php.jpg"},
        {"course":"Kotlin","img":"img/kotlin.jpg"},
        {"course":"Android Studio","img":"img/android.jpg"},
        {"course":"HTML","img":"img/html.jpg"},
    ]

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["object_list"] = self.course
            return context
        

def loginView(request):
    if request.method == "POST":
        uname = request.POST['username']
        pw = request.POST['password']
        akun = authenticate(username = uname, password = pw)
        if akun is not None:
            print("ada akun")
            login(request, akun)
            return redirect('/')
        else:
            print("Tidak ada akun")
    return render(request,'login.html')

def logoutView(request):
    logout(request)
    return redirect('/login/')

class CourseListView(ListView):
    model = Soal
    template_name = 'course.html'

    def get(self,request,*args, **kwargs):
        self.object_list = self.get_queryset().filter(course = kwargs['course'])
        title = kwargs['course']
        context = {
            "object_list":self.object_list,
            "title":title,
        }
        if "category" in request.GET:
            category = request.GET['category']
            self.object_list = self.object_list.filter(category = category)
            context['object_list'] = self.object_list
        # if "status" in request.GET:
        #     status = request.GET['status']
        #     self.object_list = self.object_list.filter(status = status)
        #     context['object_list'] = self.object_list
        

        return render(request,self.template_name,context)

class SubmitView(View):

    def get(self,request, *args, **kwargs):
        soal = Soal.objects.get(id = kwargs['id'])
        context = {
            "soal":soal,
        }
        title = kwargs['course']
        
        return render(request, 'Submit.html',context)

    def post(self,request,*args, **kwargs):
        soal = Soal.objects.get(id = kwargs['id'])
        course = soal.course
        UserSubmit.objects.create(
            user = request.user,
            soal = soal,
            jawaban = request.POST['answer'],
        )
        return redirect(f'/{course}/')