from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def other(request):
    return render(request, 'app/other.html')

def rel(request):
    return render(request, 'app/relative_url_templates.html')