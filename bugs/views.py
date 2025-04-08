from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def projects(request):
    # create projects info to be shown on the page
    projects = [
        {
            'title': 'Project 1',
            'description': 'This is a project description',
            'owner': 'John Doe',
            'bug_count': 3,
            id: 1
        },
        {
            'title': 'Project 2',
            'description': 'This is a project description',
            'owner': 'Jane Doe',
            'bug_count': 2,
            id: 2
        },
        {
            'title': 'Project 3',
            'description': 'This is a project description',
            'owner': 'John Doe',
            'bug_count': 1,
            id: 3
        }
        
    ]
    return render(request, 'project_list.html', {'projects': projects})

def create_project(request):
    return render(request, 'create_project.html')

def edit_project(request):
    # temporary project data
    project = {
            'title': 'Project 1',
            'description': 'This is a project description',
    }

    return render(request, 'edit_project.html', {'project': project})

def bugs(request):
    # return render(request, 'bugs.html')

    # create bugs info to be shown on the page
    bugs = [
        {
            'id': 1,
            'title': 'Bug 1',
            'description': 'This is a bug description',
            'status': 'Open',
            'created_at': 'January 1, 2021',
            'updated_at': 'January 1, 2021',
            'priority': 'High'
        },
        {
            'id': 2,
            'title': 'Bug 2',
            'description': 'This is a bug description',
            'status': 'Closed',
            'created_at': 'February 1, 2022',
            'updated_at': 'February 23, 2022',
            'priority': 'Low'
        },
        {
            'id': 3,
            'title': 'Bug 3',
            'description': 'This is a bug description',
            'status': 'Open',
            'created_at': 'March 1, 2023',
            'updated_at': 'March 1, 2023',
            'priority': 'Medium'
        }
    ]
    return render(request, 'bug_list.html', {'bugs': bugs})

def create_bug(request):
    return render(request, 'create_bug.html')

def edit_bug(request):
    # temporary bug data
    bug = {
            'id': 3,
            'title': 'Bug 3',
            'description': 'This is a bug description',
            'status': 'Closed',
            'created_at': 'March 1, 2023',
            'updated_at': 'March 1, 2023',
            'priority': 'Medium'
    }

    return render(request, 'edit_bug.html', {'bug': bug})