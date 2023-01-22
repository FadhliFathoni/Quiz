from django.urls import path
from . import views

urlpatterns = [
    path('',views.managerView),
    path('create/',views.SoalView.as_view()),
    path('<int:id>/delete',views.deleteView, name="delete"),
    path('<int:id>/update',views.SoalView.as_view(model = "update")),
    path('<str:username>/',views.detailJUser.as_view()),
]
