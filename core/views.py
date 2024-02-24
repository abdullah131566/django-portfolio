from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'core/index.html')


def services(request):
    return render(request, 'core/services.html')


def skills(request):
    return render(request, 'core/skills.html')


def contact(request):
    return render(request, 'core/contact.html')
