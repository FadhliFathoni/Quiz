from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SoalListView.as_view()),
    path('login/',views.loginView),
    path('logout/',views.logoutView),
    path('manager/',include('manager.urls')),
    path('<str:course>/',views.CourseListView.as_view()),
    path('<str:course>/<int:id>',views.SubmitView.as_view(), name="soal"),
]
