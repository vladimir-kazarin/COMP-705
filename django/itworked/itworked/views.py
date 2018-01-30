from django.shortcuts import render

def home(request):
    '''
    Renders home page
    '''
    greeting = "uStidy - the best study site in the world!"
    # a dictionary with a keyword 'our_greeting' mapping to the variable greeting defined above
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    context = {'our_greeting':greeting, 'weekday_list':days_of_week}
    return render(request, 'home.html', context)
