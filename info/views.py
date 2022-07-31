from django.shortcuts import render
from .models import Home, About, Project, Contact

def homePage(request):
    home = Home.objects.last()
    context = {'home': home, 'section': 'home'}
    return render(request, 'info/index.html', context)

def aboutPage(request):
    about = About.objects.last()
    context = {'about': about, 'section': 'about'}
    return render(request, 'info/about.html', context)

def projectsPage(request):
    projects = Project.objects.all()
    context = {'projects': projects, 'section': 'projects'}
    return render(request, 'info/projects.html', context)

def contactPage(request):
    contact = Contact.objects.last()
    context = {'contact': contact, 'section': 'contact'}
    return render(request, 'info/contact.html', context)
