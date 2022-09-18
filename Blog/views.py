from django.shortcuts import render
from .forms import BlogForm
from .models import Blog

# Create your views here.


def add_blog(request):
    '''Form to add the blog..'''

    if request.method=='POST':
        form=BlogForm(request.POST)
        if form.is_valid():
               content=form.cleaned_data['content']
               title=form.cleaned_data['title']
               author=form.cleaned_data['author']
               blog=Blog(content=content,title=title,author=author)
               blog.save()
               return render(request,'blog_detail.html',{'blog':blog})
    else:
        form=BlogForm()
        return render(request,'blog_form.html',{'form':form})

def blog_detail(request,blogid):

    '''Blog displayed in detail...'''

    blog=Blog.objects.get(pk=blogid)
    return render(request,'blog_detail.html',{'blog':blog})

