from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from datetime import date

all_posts = [
    {
    "slug": "programming",
    "image": "coding.jpg",
    "author": "Kamil Adaszewski",
    "date": date(2023, 3, 3),
    "title": "Computer Programming",
    "excerpt": "Programming is the most important skill in the 21th Century!",
    "content":"Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nobis, veritatis, blanditiis nostrum possimus, quidem eius repellat rem fuga soluta doloremque modi praesentium quisquam voluptatum maiores? Expedita voluptates nobis voluptatum natus!",

    },
    {
    "slug": "mountain",
    "image": "mountains.jpg",
    "author": "Kamil Adaszewski",
    "date": date(2023, 3, 2),
    "title": "Mountain Hiking",
    "excerpt": "How to climb on the mount everest",
    "content":"Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nobis, veritatis, blanditiis nostrum possimus, quidem eius repellat rem fuga soluta doloremque modi praesentium quisquam voluptatum maiores? Expedita voluptates nobis voluptatum natus!",
    
    },
    {
    "slug": "nature",
    "image": "woods.jpg",
    "author": "Kamil Adaszewski",
    "date": date(2023, 3, 1),
    "title": "Nature and health",
    "excerpt": "Be present and enjoy nature, stay healthy as much as you can",
    "content":"Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nobis, veritatis, blanditiis nostrum possimus, quidem eius repellat rem fuga soluta doloremque modi praesentium quisquam voluptatum maiores? Expedita voluptates nobis voluptatum natus!",
    
    },
]

def get_date(post):
    return post.get('date')

def start(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/posts.html",{
        "all_posts": all_posts
    })

def post_detail(request, slug):
    indetified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html",{
        "post": indetified_post
    })