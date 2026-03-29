# DjangoLab - Lab Manual Projects

A comprehensive Django learning workspace containing multiple practical lab exercises covering Django fundamentals to advanced features.

## 📁 Project Structure

```
DjangoLab/
├── env/                          # Virtual Environment (Python 3.11)
│   └── Scripts/
│       └── Activate.ps1         # Activation script for Windows
│
├── myproject/                    # Main Django Project
│   ├── README.md                # Detailed project documentation
│   ├── manage.py
│   ├── db.sqlite3
│   │
│   ├── myproject/               # Project configuration
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   └── app1-app5/               # 5 Django applications
│       └── (See myproject/README.md for details)
│
├── .git/                         # Git version control
├── .gitignore                    # Git ignore rules
└── README.md                     # This file
```

## 🚀 Quick Start

### 1️⃣ Activate Virtual Environment
```powershell
cd d:\DjangoLab
.\env\Scripts\Activate.ps1
```

You should see `(env)` in your terminal prompt.

### 2️⃣ Navigate to Project
```powershell
cd myproject
```

### 3️⃣ Apply Migrations
```powershell
python manage.py migrate
```

### 4️⃣ Create Superuser (for admin access)
```powershell
python manage.py createsuperuser
```

### 5️⃣ Run Development Server
```powershell
python manage.py runserver
```

Server runs at: **http://127.0.0.1:8000/**

---

## 📚 What's Inside

This workspace contains **5 Django applications** implementing lab manual questions:

| App | Program | Topic | URL |
|-----|---------|-------|-----|
| **app1** | Program 3 | Table of Squares | `/cts/<int:s>/<int:n>` |
| **app2** | Program 4 | Vowels & Consonants | `/vc/<str:sentence>/` |
| **app3** | Program 5 | Prime Number Checker | `/prime/` |
| **app4** | Programs 6 & 7 | Student-Course Models & Admin | `/admin/` |
| **app5** | Program 8 | Class-Based Views | `/app5/students/` |

---

## 📖 For Detailed Information

👉 **See [myproject/README.md](myproject/README.md)** for:
- Detailed explanation of each application
- Complete project structure
- Usage examples for each feature
- Troubleshooting guide
- Learning outcomes

---

## 🛠️ Environment Details

- **Python**: 3.11
- **Django**: 5.2.12
- **Database**: SQLite3
- **Virtual Environment Location**: `.\env\`

---

## 📋 Common Commands

```powershell
# Activate venv
.\env\Scripts\Activate.ps1

# Navigate to project
cd myproject

# Run server
python manage.py runserver

# Access Django shell
python manage.py shell

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Access admin
# Visit: http://127.0.0.1:8000/admin/
```

---

## 📌 Important Notes

✅ **Always activate the virtual environment** before running commands

✅ **Always run** `python manage.py migrate` after activating the environment for the first time

✅ **Use `..\env\Scripts\Activate.ps1`** from within `myproject/` folder if needed

❌ **Don't modify `env/` folder** - it contains all dependencies

---

## 🎓 Learning Path

1. Start with **App1** - Simple URL routing and views
2. Move to **App2** - String processing and URL parameters
3. Try **App3** - Logic and conditionals
4. Explore **App4** - Database models and relationships
5. Master **App5** - Advanced class-based views

---

## 📚 Project Documentation Tree

```
DjangoLab/
└── myproject/README.md          ← Detailed project docs
    ├── App1: Table of Squares
    ├── App2: Vowels & Consonants
    ├── App3: Prime Checker
    ├── App4: Student-Course Models
    └── App5: Class-Based Views
```

---

## ✨ Get Started Now!

1. Open PowerShell in `d:\DjangoLab`
2. Run: `.\env\Scripts\Activate.ps1`
3. Navigate: `cd myproject`
4. Run: `python manage.py runserver`
5. Open browser: `http://127.0.0.1:8000/`(local host)

**Happy Learning!** 🎓
