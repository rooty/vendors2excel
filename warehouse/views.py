import os
from django.shortcuts import render_to_response
from django.conf import settings

def home(request):
    print settings.COMPRESS_REVISION_NUMBER
    return render_to_response('index.html')
