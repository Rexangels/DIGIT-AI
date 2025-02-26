from django.shortcuts import render
from digit_ai.models import Project

def dashboard(request):
    projects = Project.objects.all()
    current_project = projects.first() if projects.exists() else None
    return render(request, 'dashboard.html', {
        'projects': projects,
        'current_project': current_project
    })
