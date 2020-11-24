
from django.urls import path,include

from . import views

app_name='blog'
urlpatterns = [


    path('',views.Blog,name='blog'),
    path('<int:blog_id>/',views.details,name='details'),
]