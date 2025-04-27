from django.contrib import admin

# Register your models here.
from .models import Bug
from .models import Project
from .models import User

# Set up the admin interface for the Bug, Project, and User models

class BugAdmin(admin.ModelAdmin):
    # display the fields in the admin interface
    list_display = ('title', 'status', 'created_at', 'updated_at', 'project', 'reporter')
    # set the ordering of the fields in the admin interface
    ordering = ('created_at',)
admin.site.register(Bug, BugAdmin)

class ProjectAdmin(admin.ModelAdmin):
    # display the fields in the admin interface
    list_display = ('title', 'created_at', 'updated_at', 'bug_count', 'owner')
    # set the ordering of the fields in the admin interface
    ordering = ('created_at',)
admin.site.register(Project, ProjectAdmin)

class UserAdmin(admin.ModelAdmin):
    # display the fields in the admin interface
    list_display = ('username',)
    # set the ordering of the fields in the admin interface
    ordering = ('username',)
admin.site.register(User, UserAdmin)
