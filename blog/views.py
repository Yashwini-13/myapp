from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging

# Create your views here.
posts = [
        {'id':1,'title': 'Post 1','content':'Content of post 1'},
        {'id':2,'title': 'Post 2','content':'Content of post 2'},
        {'id':3,'title': 'Post 3','content':'Content of post 3'},
        {'id':4,'title': 'Post 4','content':'Content of post 4'}
    ]
def index(request):
    blog_title = "Latest Posts"
    return render(request,'blog/index.html', {'blog_title': blog_title,'posts': posts})

def detail(request, post_id):
    post = next((item for item in posts if item['id'] == post_id), None)
    logger = logging.getLogger("TESTING") 
    logger.debug(f'post variable is {post}')
    return render(request,'blog/detail.html',{'post': post})

    
def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is the new url")



