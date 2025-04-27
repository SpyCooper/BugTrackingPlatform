# BugTrackingPlatform

## Description
A website that uses django to organize projects and bugs that a user can see.

After logging in, the user can see all the projects they are a part of. Each project has an edit button where the user can edit the project or delete it only if the user is the owner/creator of that project. Clicking on a project will show the bugs list. You can create a new project with a button at the bottom of the screen.

In the bugs list, the user can see all the bugs for that specific project. They can create a new bug with the button at the bottom of the screen or can edit a bug by clicking on it. There is also a back to project button at tht top left of the screen.

When the user is looking at the projects list or bugs list, they can log out with the log out button on the top right of the screen.

There is some built in features where an account named `admin` will be automatically added to a team members list if they aren't selected as a team member and if `admin` exists.

## Features
- Users can login, be added to projects, and only see projects they are in.
- Create, update, and delete projects.
- Create, update, and delete bugs within projects.

## Folder Structure
The only two folders in here are the both django apps.
- `bugtracking` -  the default django application that is created
- `tracker` - the django app that is the actually bug tracker

## Installation and Execution

1. **Clone the Repository**  
    Clone this repository to your machine using:
    ```bash
    git clone <repository-url>
    ```

2. **Navigate to the Project Directory**  
    ```
    cd BugTrackingPlatform
    ```

3. **Create a Virtual Environment**  
    Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

4. **Install Dependencies**  
    Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

5. **Apply Migrations**  
    Run the following commands to set up the database:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Run the Development Server**  
    Start the Django development server:
    ```bash
    python manage.py runserver
    ```

7. **Access the Application**  
    Open your browser and navigate to `http://127.0.0.1:8000/`.

8. **Create a Superuser/Admin (Optional)**  
    To access the admin panel, create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to set up the superuser credentials.

9. **Access Superuser/Admin Panel (Optional)** 
    Navigate to `http://127.0.0.1:8000/admin` and login with the new superuser account to see the database.
