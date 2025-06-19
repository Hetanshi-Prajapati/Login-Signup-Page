# Django Login and Signup System

This is a fully functional Django-based **Login and Signup System** with advanced authentication features, social logins, CAPTCHA protection, and password management.

### Login Page
- Username and Password Authentication
- CAPTCHA (Refreshes on Reload)
- "Remember Me" Option
- Forgot Password with Email Reset
- Social Login: Google & Facebook Integration
- Login redirects to the Dashboard/Home page

### Signup Page
- Username, Email, Password, and Confirm Password
- Google & Facebook Social Signup
- Redirect links: Login ➡ Signup and Signup ➡ Login

### Database
- MySQL backend to securely store user data and credentials

### Additional Highlights
- Django Authentication System
- CAPTCHA Integration
- Social Authentication using Google and Facebook OAuth
- User session management with "Remember Me" functionality
- Proper form validation and error handling

## Technologies Used
- Python
- Django
- MySQL Workbench
- Google OAuth 
- Facebook OAuth 
- CAPTCHA
- HTML, CSS (Bootstrap)

## Project Structure
```text
Login-System/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── myproject/
│   ├── settings.py (Secret key removed)
│   ├── urls.py
│
├── accounts/  # Django App
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── templates/
│   │   ├── login.html
│   │   ├── signup.html
│   │   ├── lgsuccess.html
│   ├── static/
│
├── templates/
├── static/
