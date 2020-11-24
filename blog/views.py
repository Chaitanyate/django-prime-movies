from django.shortcuts import render,get_object_or_404
from .models import blog
def Blog(request):
    b=blog.objects.all()

    return render(request,'blogs/blog.html',{'B':b})

def details(request,blog_id):
    bg=get_object_or_404(blog,pk=blog_id)
    return render(request,'blogs/details.html',{'id':bg})



