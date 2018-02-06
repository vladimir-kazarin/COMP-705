from django.shortcuts import render

def home(request):
    """
    Renders home page.
    """
    context = {}
    return render(request, 'home.html', context)

def resume(request):
    """
    Renders resume page.
    """
    context = {}
    return render(request, 'resume.html', context)

def portfolio(request):
    """
    Renders portfolio page.
    """
    context = {}
    return render(request, 'portfolio.html', context)

def contact(request):
    """
    Renders contact page.
    """
    context = {}
    return render(request, 'contact.html', context)
