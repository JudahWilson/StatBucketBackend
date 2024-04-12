from django.shortcuts import render
from django.http import HttpResponse


def htmx(request):
    # generate random float
    import random
    random_float = random.random()

    return HttpResponse(random_float)