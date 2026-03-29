# Django Lab Manual - Programs 3 to 9

A comprehensive Django project demonstrating various web development concepts through practical lab exercises. This project implements multiple applications covering Django fundamentals to advanced features.

## 📋 Project Overview

This is a Django 5.2.12 project containing multiple applications (App1-App5) that progressively demonstrate Django concepts through hands-on implementations.

## 🗂️ Project Structure

```
myproject/
├── manage.py                 # Django management script
├── db.sqlite3               # Development database
├── README.md               # This file
│
├── myproject/              # Project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── __init__.py
│
├── app1/                   # Program 3: Table of Squares
├── app2/                   # Program 4: Vowels & Consonants Counter
├── app3/                   # Program 5: Prime Number Checker
├── app4/                   # Programs 6 & 7: Student-Course Management (Models & Admin)
└── app5/                   # Program 8: Class-Based Views (Student List & Detail)
```

---

## 📚 Applications Overview

### **App1 - Program 3: Table of Squares**
**Question**: Develop a Django application that displays tables of squares of pairs of numbers input through the URL.

**URL**: `/cts/<int:s>/<int:n>`
- `s`: Starting number
- `n`: Number of entries

**Example**: `/cts/1/5` displays squares from 1 to 5

**Files**:
- `app1/views.py`: Main view logic
- `app1/urls.py`: URL patterns

---

### **App2 - Program 4: Vowels & Consonants Counter**
**Question**: Develop a Django application that displays the number of vowels and consonants and also lists them for any input sentence specified in the URL.

**URL**: `/vc/<str:sentence>/`
- `sentence`: Any text string to analyze

**Example**: `/vc/hello%20world/` analyzes the sentence "hello world"

**Features**:
- Counts vowels and consonants
- Lists individual vowels and consonants
- Handles URL-encoded strings

**Files**:
- `app2/views.py`: Vowel/Consonant analysis logic
- `app2/urls.py`: URL patterns

---

### **App3 - Program 5: Prime Number Checker**
**Question**: Develop a Django project to check whether a given number is prime or not.

**URL**: `/prime/`

**Features**:
- Input interface to check if a number is prime
- Mathematical validation
- Display results

**Files**:
- `app3/views.py`: Prime number checking logic
- `app3/templates/`: HTML templates for UI

---

### **App4 - Programs 6 & 7: Student-Course Management**
**Questions**: 
- Program 6: Develop a Django application that performs student registration to a course
- Program 7: Register admin interfaces, perform migrations, and illustrate data entry

**Models**:

```python
class Student(models.Model):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    email = EmailField(unique=True)

class Course(models.Model):
    name = CharField(max_length=100)
    description = TextField()
    students = ManyToManyField(Student, related_name='courses')
```

**Admin Interface**: 
- Register Student and Course models in Django Admin
- Add/Edit/Delete students and courses
- Manage many-to-many relationships

**URL**: `/admin/`

**Files**:
- `app4/models.py`: Student and Course models
- `app4/admin.py`: Admin registration
- `app4/urls.py`: URL patterns
- `app4/migrations/`: Database migrations

---

### **App5 - Program 8: Class-Based Views**
**Question**: Create generic class-based views that display a list of students and a detailed view for any selected student.

**URLs**:
- `/app5/students/` - Display list of all students
- `/app5/students/<int:pk>/` - Display details of a specific student

**Views**:

```python
class StudentListView(ListView):
    model = Student
    template_name = 'app5/student_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'app5/student_detail.html'
    context_object_name = 'student'
```

**Templates**:
- `app5/templates/app5/student_list.html`: List view template
- `app5/templates/app5/student_detail.html`: Detail view template

**Files**:
- `app5/views.py`: Class-based views
- `app5/urls.py`: URL routing
- `app5/templates/`: HTML templates

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Django 5.2.12
- Virtual Environment

### Installation

1. **Navigate to the project directory**:
   ```powershell
   cd d:\DjangoLab\myproject
   ```

2. **Activate the virtual environment**:
   ```powershell
   ..\env\Scripts\Activate.ps1
   ```
   
   You should see `(env)` in your prompt.

3. **Apply migrations** (sets up database tables):
   ```powershell
   python manage.py migrate
   ```

4. **Create a superuser** (for admin access):
   ```powershell
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin account.

5. **Run the development server**:
   ```powershell
   python manage.py runserver
   ```

   The server will start at `http://127.0.0.1:8000/`

---

## 📖 Usage Guide

### Testing Each Application

#### **App1 - Table of Squares**
Navigate to: `http://127.0.0.1:8000/cts/2/5`
- Shows squares from 2 to 6

#### **App2 - Vowels & Consonants**
Navigate to: `http://127.0.0.1:8000/vc/hello/`
- Analyzes the word "hello"

#### **App3 - Prime Checker**
Navigate to: `http://127.0.0.1:8000/prime/`
- Opens form to check prime numbers

#### **App4 - Admin Interface**
Navigate to: `http://127.0.0.1:8000/admin/`
- Login with superuser credentials
- Add/manage students and courses
- Create many-to-many relationships

#### **App5 - Student Views**
Navigate to: `http://127.0.0.1:8000/app5/students/`
- View list of all students
- Click on a student to see detailed information

---

## 🔧 Management Commands

```powershell
# Apply migrations
python manage.py migrate

# Create migrations for model changes
python manage.py makemigrations

# Create a superuser
python manage.py createsuperuser

# Run the development server
python manage.py runserver

# Access Django shell
python manage.py shell

# Collect static files (for production)
python manage.py collectstatic
```

---

## 📋 Installed Apps

The project includes the following Django apps:
- **django.contrib.admin** - Admin interface
- **django.contrib.auth** - Authentication system
- **django.contrib.contenttypes** - Content type framework
- **django.contrib.sessions** - Session management
- **django.contrib.messages** - Messaging framework
- **django.contrib.staticfiles** - Static files management
- **app1** - Table of squares
- **app2** - Vowels & consonants counter
- **app3** - Prime number checker
- **app4** - Student-course management
- **app5** - Class-based views for students

---

## 🗄️ Database Models

### Student Model (App4)
```
- first_name: CharField(max_length=50)
- last_name: CharField(max_length=50)
- email: EmailField(unique=True)
```

### Course Model (App4)
```
- name: CharField(max_length=100)
- description: TextField()
- students: ManyToManyField(Student)
```

---

## 📝 Notes

- **Debug Mode**: Currently enabled (`DEBUG = True` in settings.py). Disable in production.
- **Database**: Using SQLite3 (`db.sqlite3`). Consider PostgreSQL for production.
- **Secret Key**: Keep the SECRET_KEY in settings.py secure and use environment variables in production.
- **Virtual Environment**: Always work within the virtual environment to avoid dependency conflicts.

---

## 🐛 Troubleshooting

### Issue: "No module named 'django'"
- **Solution**: Activate the virtual environment and install Django:
  ```powershell
  pip install django
  ```

### Issue: "ModuleNotFoundError: No app with label 'app5'"
- **Solution**: Ensure all apps are listed in `INSTALLED_APPS` in settings.py

### Issue: "Unapplied migrations"
- **Solution**: Run `python manage.py migrate`

### Issue: Student detail view not showing data
- **Solution**: Ensure the `context_object_name` in App5 DetailView is set to `'student'` (singular)

---

## 📚 Learning Outcomes

Upon completing this project, you will understand:
1. ✅ Basic URL routing and view functions
2. ✅ Template rendering and context passing
3. ✅ Model creation and relationships (ManyToMany)
4. ✅ Django Admin interface customization
5. ✅ Database migrations
6. ✅ Class-based views (ListView, DetailView)
7. ✅ Template inheritance and static files
8. ✅ Form handling and validation

---

## 📖 Resources

- [Django Official Documentation](https://docs.djangoproject.com/en/5.2/)
- [Django Generic Class-Based Views](https://docs.djangoproject.com/en/5.2/topics/class-based-views/)
- [Django Models](https://docs.djangoproject.com/en/5.2/topics/db/models/)
- [Django Admin](https://docs.djangoproject.com/en/5.2/ref/contrib/admin/)

---

## 📄 License

This project is for educational purposes as part of a Django lab manual.

---

## ✨ Summary

This project provides a hands-on learning experience with Django, progressing from simple URL routing to complex features like class-based views and model relationships. Each application builds upon previous knowledge, making it an excellent resource for Django beginners.

**Happy Learning!** 🎓
