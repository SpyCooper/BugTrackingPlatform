from django.shortcuts import render, redirect
from .models import User, Project, Bug
from .forms import BugForm, ProjectForm, RegisterForm

# create views for the bugs app

# define the login view
def login(request):
    # read input from the user
    if request.method == 'POST':
        # get the username and password from the request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if the username and password are valid
        try:
            User.objects.get(username=username, password=password)
            request.session['username'] = username
            # redirect to the projects page if the login is successful
            return redirect('projects')
        # if the username and password are invalid, show an error message
        except User.DoesNotExist:
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})
    
    # if the request method is GET, render the login page
    return render(request, 'login.html')


# define the register view
def register(request):
    # read input from the user
    if request.method == 'POST':
        # get the input data in the form
        form = RegisterForm(request.POST)

        # check if the form is valid
        if form.is_valid():
            # check if the password and confirm password fields match
            try:
                # save the user instance
                user = form.save(commit=False)
                user.password = form.cleaned_data['password']  # Set the password

                # save the user instance to the database
                user.save()

                # redirect to the login page after successful registration
                return redirect('login')
            
            # if there is an error while saving the user instance, show an error message
            except Exception as e:
                return render(request, 'register.html', {'form': form, 'error_message': str(e)})
    
    # if the request method is GET, render the register page
    return render(request, 'register.html', {'form': RegisterForm()})


# define the projects view
def projects(request):
    # check if the request method is POST
    if request.method == 'POST':
        # get the action from the request and perform the corresponding action
        action = request.POST.get('action')
        if action == 'create_project':
            return redirect('create_project')
        elif action == 'edit_project':
            return redirect('edit_project', project_id=request.POST.get('project_id'))
        elif action == 'view_project':
            # redirect to the bugs page for the selected project
            project_id = request.POST.get('project_id')
            return redirect('bugs', project_id=project_id)

    # get the logged-in user from the session
    username = request.session.get('username')

    # if the user is logged in
    if username:
        # get the projects for the logged-in user
        user = User.objects.filter(username=username).first()
        if user:
            projects = Project.objects.filter(team_members=user).order_by('created_at')
        else:
            return render(request, 'project_list.html', {'error_message': "Logged-in user not found"})
    # if there is no logged-in user, show an error message
    else:
        return render(request, 'project_list.html', {'error_message': "User not logged in"})    
    
    # render the project list page with the projects for the logged-in user
    return render(request, 'project_list.html', {'projects': projects, 'user': user})


# define the create project view
def create_project(request):
    # check if the request method is POST
    if request.method == 'POST':
        # get the form data from the request
        form = ProjectForm(request.POST)

        # check if the form is valid
        if form.is_valid():
            team_members = form.cleaned_data.get('team_members')
            current_user = User.objects.get(username=request.session.get('username'))

            # check if the current user is already in the team members list
            if current_user not in team_members:
                # add the current user to the team members list
                team_members = list(form.cleaned_data['team_members'])
                team_members.append(current_user)
                form.cleaned_data['team_members'] = team_members

            # check if the admin user exists and is not already in the team members list
            if not User.objects.filter(username='admin').exists() or User.objects.get(username='admin') not in form.cleaned_data['team_members']:
                # add the admin to the team members list
                team_members = list(form.cleaned_data['team_members'])
                team_members.append(User.objects.get(username='admin'))
                form.cleaned_data['team_members'] = team_members

            # create the project instance but don't save it yet
            project = form.save(commit=False)

            # set the owner of the project to the logged-in user
            try:
                project.owner = current_user
                project.bug_count = 0
                project.save()
                form.save_m2m()  # Save the many-to-many relationship with team members
            # if the user does not exist, show an error message
            except User.DoesNotExist:
                return render(request, 'create_project.html', {'form': form, 'error_message': "Logged-in user not found"})

            # redirect to the projects page after successful project creation
            return redirect('projects')
        # if the form is not valid, show an error message
        else:
            return render(request, 'create_project.html', {'form': form, 'error_message': "Invalid form data"})

    # if the request method is GET, render the create project page
    return render(request, 'create_project.html', {'form': ProjectForm()})


# define the edit project view
def edit_project(request, project_id):
    # get the project instance from the database
    project = Project.objects.filter(id=project_id).first()

    # check if the project exists
    if not project:
        return render(request, 'edit_project.html', {'error_message': "Project not found"})
    
    # check if the request method is POST
    if request.method == 'POST':
        # get the action from the request and perform the corresponding action
        action = request.POST.get('action')

        # check if the action is to delete the project
        if action == 'delete_project':
            # remove the project and all of the bugs from the database
            Bug.objects.filter(project=project).delete()
            project.delete()
            return redirect('projects')
        
        # create a form instance with the POST data and the project instance
        form = ProjectForm(request.POST, instance=project)
        # check if the form is valid
        if form.is_valid():
            # save the project instance to the database
            form.save()
            # redirect to the projects page after successful project update
            return redirect('projects')
        
        # if the form is not valid, show an error message
        return render(request, 'edit_project.html', {'project': project, 'form': form, 'error_message': "Invalid form data"})
    
    # if the request method is GET, create a form instance with the project instance and render the edit project page
    form = ProjectForm(instance=project)
    # set the help text for the team members field
    form.fields['team_members'].help_text = "Control + click to select multiple team members"
    return render(request, 'edit_project.html', {'project': project, 'form': form})


# define the bugs view
def bugs(request, project_id):
    # check if the project exists
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return render(request, 'bug_list.html', {'error_message': "Project not found"})
    
    # get the bugs for the project
    bugs = Bug.objects.filter(project=project).order_by('created_at')

    # check if the request method is POST
    if request.method == 'POST':
        # get the action from the request and perform the corresponding action
        action = request.POST.get('action')
        if action == 'create_bug':
            return redirect('create_bug', project_id=project_id)
        elif action == 'edit_bug':
            bug_id = request.POST.get('bug_id')
            return redirect('edit_bug', project_id=project_id, bug_id=bug_id)
    
    # render the bug list page with the bugs for the project
    return render(request, 'bug_list.html', {'bugs': bugs, 'project': project, 'project_title': project.title})


# define the create bug view
def create_bug(request, project_id):
    # check if the project exists
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return render(request, 'create_bug.html', {'error_message': "Project not found"})
    
    # check if the request method is POST
    if request.method == 'POST':
        # create a form instance with the POST data
        form = BugForm(request.POST)
        # check if the form is valid
        if form.is_valid():
            # create the bug instance but don't save it yet
            bug = form.save(commit=False)
            bug.project = project  # Associate the bug with the current project
            try:
                bug.reporter = User.objects.get(username=request.session.get('username'))  # Associate the bug with the logged-in user
                bug.save() # Save the bug instance to the database
                project.bug_count += 1  # Increment the bug count for the project
                project.save() # Save the project instance to the database
            # if the user does not exist, show an error message
            except User.DoesNotExist:
                return render(request, 'create_bug.html', {'form': form, 'error_message': "Logged-in user not found", 'project': project})
            
            # redirect to the bugs page after successful bug creation
            return redirect('bugs', project_id=project_id)
        # if the form is not valid, show an error message
        else:
            return render(request, 'create_bug.html', {'form': form, 'error_message': "Invalid form data", 'project': project})
    
    # if the request method is GET, create a form instance and render the create bug page
    return render(request, 'create_bug.html', {'form': BugForm(), 'project': project})


# define the edit bug view
def edit_bug(request, project_id, bug_id):
    # check if the project exist
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return render(request, 'edit_bug.html', {'error_message': "Project not found"})
    
    # check if the bug exists
    try:
        bug = Bug.objects.get(id=bug_id, project=project)
    except Bug.DoesNotExist:
        return render(request, 'edit_bug.html', {'error_message': "Bug not found"})
    
    # check if the request method is POST
    if request.method == 'POST':
        # get the action from the request and perform the corresponding action
        action = request.POST.get('action')
        if action == 'delete_bug':
            # remove the bug from database and decrement the bug count for the project
            bug.delete()
            project.bug_count -= 1
            project.save()
            return redirect('bugs', project_id=project_id)
        # check if the action is to update the bug
        else:
            form = BugForm(request.POST, instance=bug)
            # check if the form is valid
            if form.is_valid():
                # save the bug instance to the database
                form.save()
                return redirect('bugs', project_id=project_id)
            # if the form is not valid, show an error message
            else:
                return render(request, 'edit_bug.html', {'bug': bug, 'form': form, 'error_message': "Invalid form data", 'project': project})
    
    # if the request method is GET, create a form instance with the bug instance and render the edit bug page
    return render(request, 'edit_bug.html', {'bug': bug, 'form': BugForm(instance=bug), 'project': project})
