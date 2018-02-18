from django.shortcuts import render
from .models import Education, Experience

# Create your views here.
def home(request):
    '''
    Renders the Resume app home page
    '''
    education_qs = Education.objects.all()
    experience_qs = Experience.objects.order_by('-start_date')
    context = {'education_list': education_qs,
     'experience_list': experience_qs}
    return render(request, 'resume/home.html', context) 
