from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return html string rendered by django not using a template
    return render(request, 'index.html', {'title': 'Hello HTMX and Django'})
    
def htmx(request):
    # generate random float
    import random
    random_float = random.random()
    
    return HttpResponse(random_float)