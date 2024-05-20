from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('add',views.add,name="add"),
    path('edit',views.Edit,name="edit"),
    path('update/<str:id>',views.Update,name="update"),



        ]