from django.shortcuts import render, get_object_or_404
from .models import Post
posts =[Post(i,i+1,i)  for i in range(10)]
def post_list(request):  # Display posts in descnding order
    return render(request, 'showposts/post_list.html', {'posts': posts})

def post_content(request,pk=None):
    post = posts[pk]
    print("PK",pk)
    return render(request, 'showposts/post_content.html', {'post': post})