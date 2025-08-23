from django.shortcuts import render

def index(request):
    context = {'page_title': 'Welcome to my Django App'}
    return render(request, 'posts/index.html', context)
