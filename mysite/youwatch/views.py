from django.shortcuts import render
import os

index_vids = []
for i in range(30): # This is the number of placeholder videos generated in the index.html page.
    index_vids.append(i)


# Create your views here.
def index(request):
    return render(request, "youwatch/index.html", {
        "index_vids": index_vids
    })

trending_videos = []
for i in range(1, 11):
    trending_videos.append(i)

def trending(request):
    return render(request, "youwatch/trending.html", {
        "trending_videos": trending_videos
    })

def upload(request):
    return render(request, "youwatch/upload.html")

def categories(request):
    return render(request, "youwatch/categories.html")

def player(request):
    return render(request, "youwatch/sample_player.html", {
        "videos": ["video.mp4"]
    })