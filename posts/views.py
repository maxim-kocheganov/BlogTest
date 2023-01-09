from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post as Post_model

# Create your views here.
def Index(request):    
    if request.method =="GET":
        posts = Post_model.objects.all()
        displayPosts = []
        for post in posts:
            p = {'title':post.title,
                 'author':post.creator,
                 'content':post.content,
                 'date':post.created,
                 'view': '/show/' + str(post.id),
                 'edit': '/edit/' + str(post.id),
                 'delete': '/delete/' + str(post.id)
                 }
            displayPosts.append(p)
        return render(request,"home.html",{"displayPosts":displayPosts})
