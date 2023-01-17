from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SoalListView),
    path('login/',views.loginView),
    path('manager/',include('manager.urls')),
    path('<str:course>/',views.CourseListView.as_view()),
    path('<str:course>/<int:id>',views.CourseListView.as_view()),
]
