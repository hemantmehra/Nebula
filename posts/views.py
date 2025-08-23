from django.shortcuts import render

def index(request):
    context = {'page_title': 'Welcome to my Django App'}
    return render(request, 'my_app/index.html', context)
