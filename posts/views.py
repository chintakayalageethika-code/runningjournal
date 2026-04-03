from django.shortcuts import render, get_object_or_404
from .models import Post
import requests


def home(request):
    category = request.GET.get('category')

    if category:
        posts = Post.objects.filter(category=category).order_by('-date')
    else:
        posts = Post.objects.all().order_by('-date')

    return render(request, 'posts/home.html', {
        'posts': posts,
        'category': category
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})


def strava_runs(request):
    access_token = "d7553621d77214ab83027f7e9fbdddd28fc0d753"

    url = "https://www.strava.com/api/v3/athlete/activities"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    # 🔴 HANDLE ERROR (IMPORTANT)
    if isinstance(data, dict):
        return render(request, "posts/strava.html", {
            "activities": [],
            "error": data.get("message", "Error fetching data")
        })

    # ✅ NORMAL DATA
    for run in data:
        run['distance_km'] = round(run['distance'] / 1000, 2)
        run['time_min'] = round(run['moving_time'] / 60, 1)

    return render(request, "posts/strava.html", {"activities": data})

def progress(request):
    posts = Post.objects.all()

    total_runs = posts.count()
    total_distance = sum(post.distance for post in posts if post.distance)

    return render(request, 'posts/progress.html', {
        'total_runs': total_runs,
        'total_distance': total_distance
    })