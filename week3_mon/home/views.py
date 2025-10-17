from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blog
from .forms import BlogForm
# Create your views here.

def homepage(request):
    return HttpResponse("Hey Gaurav Here learning Django")

def Student(request):
    return


def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})


def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()  # save to database
            return redirect('blog_list')  # redirect to the blog list page
    else:
        form = BlogForm()

    return render(request, 'create_blog.html', {'form': form})