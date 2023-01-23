from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate, logout
from django.views.generic.base import View
from django.views.generic import ListView
from manager.models import Soal
from .models import UserSubmit
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
 
@login_required(login_url='/login/')
def SoalListView(request):
    course = [
        {"course":"Java","img":"static/img/java.jpg"},
        {"course":"PHP","img":"static/img/php.jpg"},
        {"course":"Kotlin","img":"static/img/kotlin.jpg"},
        {"course":"Android","img":"static/img/android.jpg"},
        {"course":"HTML","img":"static/img/html.jpg"},
    ]

    context = {
        "object_list":course,
    }
    for soal in course:
        jumlahSoal = Soal.objects.filter(course = soal['course'])

        jawaban = UserSubmit.objects.filter(user = request.user)
        penampung = 0
        context[soal['course']] = 0
        for x in jawaban:
            if x.soal.course == soal['course']:
                penampung = penampung + 1
                rata = int(penampung / len(jumlahSoal) * 100)
                context[soal['course']] = rata
    return render(request, 'landingPage.html',context)
        

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
        jawaban = UserSubmit.objects.filter(user = request.user)
        title = kwargs['course']
        context = {
            "object_list":self.object_list,
            "jawaban":jawaban,
            "title":title,
        }
        if "category" in request.GET:
            category = request.GET['category']
            self.object_list = self.object_list.filter(category = category)
            context['object_list'] = self.object_list
        

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