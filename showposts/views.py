from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, PostForm
from django.db import models
def post_list(request):  # Display posts in descnding order
    posts = Post.objects.all()
    return render(request, 'showposts/post_list.html', {'posts': posts})

def post_content(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'showposts/post_content.html', {'post': post})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)  # Populate form with POST data
        if form.is_valid():
            form.save()  # Save the new post to the database
            return redirect('post_list')  # Redirect to the post list (or any other page)
    else:
        form = PostForm()  # Create an empty form for GET request

    return render(request, 'showposts/add_posts.html', {'form': form})