# TDD Django Blog Project


This Django blog project is developed to practice Test-Driven Development (TDD) concepts in programming. The project incorporates various features related to blog management, user authentication, and profile management.

## Features

### 1. List View

- **Endpoint**: `/posts/`
- Displays a list of blog posts.

### 2. Detail View

- **Endpoint**: `/posts/{post_id}/`
- Shows detailed information about a specific blog post.

### 3. User Creation Page

- **Endpoint**: `/accounts/signup/`
- Allows users to create an account.

### 4. User Signup Form and Login/Logout

- **Endpoint (Signup)**: `/accounts/signup/`
- **Endpoint (Login)**: `/accounts/login/`
- **Endpoint (Logout)**: `/accounts/logout/`
- Provides a signup form for user registration and allows users to log in/out.

### 5. Account Creation

- **Endpoint**: `/accounts/create/`
- Enables users to create and manage their accounts.

### 6. Password Management

- **Endpoint (Change Password)**: `/accounts/password/change/`
- Allows users to change their account passwords.

### 7. Creating User Profiles

- **Endpoint**: `/accounts/profile/{username}/`
- Generates user profiles with relevant information.

### 8. Edit User Profile and Add Avatars (ToDo)

- **Endpoint (Edit Profile)**: `/accounts/profile/{username}/edit/`
- Allows users to edit their profiles and upload avatars.

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/TDD-Django-Blog.git
    ```

2. **Install dependencies:**

    ```bash
    cd TDD-Django-Blog
    pip install -r requirements.txt
    ```

3. **Run migrations:**

    ```bash
    python manage.py migrate
    ```

4. **Create a superuser for admin access:**

    ```bash
    python manage.py createsuperuser
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

6. **Access the project in your browser:** [http://localhost:8000/](http://localhost:8000/)

## Testing

To run tests, use the following command:

```bash
python manage.py test
