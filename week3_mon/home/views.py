from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blog
from .forms import BlogForm
from django.shortcuts import get_object_or_404

# Create your views here.

def homepage(request):
    return render(request, 'home/home.html')


def Student(request):
    return


def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})


def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('blog_list') 
    else:
        form = BlogForm()

    return render(request, 'create_blog.html', {'form': form})


def edit_blog(request,id):
    blog = get_object_or_404(Blog,id=id)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)    
        
    return render(request,'create_blog.html',{'form':form})  


def delete_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == "POST":
        blog.delete() 
        return redirect('blog_list')
    return render(request, 'delete_blog.html', {'blog': blog})
  