from django.shortcuts import render
from .models import Education, Experience, Resume

# Create your views here.
def home(request):
    '''
    Renders the Resume app home page
    '''
    resume = Resume.objects.first()
    context = {'resume': resume}
    return render(request, 'resume/home.html', context) 
