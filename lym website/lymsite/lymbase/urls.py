from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('service/', views.service, name="service"),
    path('team/', views.team, name="team"),
    path('activity/', views.activity, name="activity"),
    path('blogs/', views.blogs, name="blogs"),
    path('blog/<str:pk>/', views.blog, name="blog"),
]


