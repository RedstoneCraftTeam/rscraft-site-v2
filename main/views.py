from django.shortcuts import render

# Create your views here.
def index(request):
    latest_news = [
        "Django 3.2 released!",
        "New features in Bootstrap 5",
        "Python 3.10 beta is out"
    ]
    context = {
        'latest_news': latest_news
    }
    return render(request, 'main/index.html')