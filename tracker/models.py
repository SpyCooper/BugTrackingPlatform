from django.db import models

# Create your models here.

# default model location: <app_name>_<model_name>
# ex: bugs_bug

# database table for the Users
class User(models.Model):
    username = models.CharField(max_length=50, unique=True) # unique=True makes the field unique in the database
    password = models.CharField(max_length=50, blank=False) # max_length is required for CharField

    # sets the string representation of the model
    def __str__(self):
        return self.username
    
    # sets the meta data for the model
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ['username']


# database table for the projects
class Project(models.Model):
    id = models.AutoField(primary_key=True) # AutoField is a primary key that automatically increments
    title = models.CharField(max_length=250) # max_length is required for CharField
    description = models.TextField(blank=True) # blank=True allows the field to be blank in the admin panel
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add=True sets the field to now when the object is first created
    updated_at = models.DateTimeField(auto_now=True) # auto_now=True updates the field to now every time the object is saved

    # add a field for the project owner
    owner = models.ForeignKey('User', on_delete=models.CASCADE, default=1) # on_delete=models.CASCADE deletes the project if the user is deleted

    # add a field for the team members
    team_members = models.ManyToManyField('User', related_name='projects', default='admin') # ManyToManyField allows multiple users to be added to the project

    # add a field for the number of bugs in the project
    bug_count = models.IntegerField(editable=False, default=0) # editable=False makes the field not editable in the admin panel
    
    # sets the string representation of the model
    def __str__(self):
        return self.title
    
    # sets the meta data for the model
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['created_at']


# database table for the bugs
class Bug(models.Model):
    id = models.AutoField(primary_key=True) # AutoField is a primary key that automatically increments
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True) # blank=True allows the field to be blank in the admin panel
    status = models.CharField(max_length=50, choices=[
        ('Open', 'Open'),
        ('Closed', 'Closed'),
    ], default='open') # default status is open
    
    # field for the original reporter of the bug
    reporter = models.ForeignKey('User', on_delete=models.CASCADE, default=1, editable=False) # on_delete=models.CASCADE deletes the bug if the user is deleted, default=1 sets the default reporter to the user with ID 1 (e.g., admin)

    # field for the project the bug is associated with
    project = models.ForeignKey('Project', on_delete=models.CASCADE, default=1) # on_delete=models.CASCADE deletes the bug if the project is deleted, default=1 sets the default project to the project with ID 1 (e.g., admin)
                                
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add=True sets the field to now when the object is first created
    updated_at = models.DateTimeField(auto_now=True) # auto_now=True updates the field to now every time the object is saved
    priority = models.CharField(max_length=50, choices=[
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ], default='medium')

    # sets the string representation of the model
    def __str__(self):
        return self.title
    
    # sets the meta data for the model
    class Meta:
        verbose_name = "Bug"
        verbose_name_plural = "Bugs"
        ordering = ['created_at']
