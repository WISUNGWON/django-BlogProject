from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

# Create your views here.


def home(request):

    blog_objects = Blog.objects

    return render(request, 'home.html', {'blogs': blog_objects})


def detail(request, blog_id):

    id_object = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'id_object': id_object})


def new(request):
    return render(request, 'new.html')


def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))
