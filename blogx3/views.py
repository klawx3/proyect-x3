from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader


from .models import Post
# Create your views here.

def index(request):
    return HttpResponse("Hola mundo!")

def post_id(request,post_id):
    post = Post.objects.filter(id=post_id).first()
    if post:
        return HttpResponse(post)
    else:
        return HttpResponse("El post {} no existe :C".format(post_id))

def posts(request):
    all_post = Post.objects.all()
    template = loader.get_template('post/all_post.html')
    context = {
        'posts': all_post,
    }
    return HttpResponse(template.render(context,request))