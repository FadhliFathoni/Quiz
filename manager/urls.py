from django.urls import path
from . import views

urlpatterns = [
    path('',views.SoalListView.as_view()),
    path('create/',views.SoalView.as_view()),
    path('<int:id>/update',views.SoalView.as_view(model = "update")),
]
