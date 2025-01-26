'''
Variables automatically provided for every template 
'''
from django.conf import settings

def global_settings(request):
    # Return a dictionary to be added to the template context
    return {'DEBUG': settings.DEBUG}
