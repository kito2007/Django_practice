from django.shortcuts import render
from .models import Project
# Create your views here.

def project_index(request):
    projects = Project.objects.all().order_by('-created_at')
    context = {'projects':projects}
    return render(request, 'project/project_index.html',context)