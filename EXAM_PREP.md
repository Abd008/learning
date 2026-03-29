# DjangoLab - Exam Preparation Quick Start

A condensed study guide for exam preparation covering Django Lab Programs 3-11.

## 📖 Available Study Guides

### Main Exam Prep Guide
👉 **[EXAM_PREP.md](myproject/EXAM_PREP.md)** - Detailed exam preparation guide

This comprehensive guide covers:
- **Program 3**: Table of Squares
- **Program 4**: Vowels & Consonants Counter
- **Program 5**: Prime Number Checker
- **Programs 6 & 7**: Models & Admin Interface
- **Program 8**: Class-Based Views
- **Program 9**: CSV & PDF Generation
- **Program 10**: AJAX Registration
- **Program 11**: AJAX Course Search

## 🎯 What's Covered

Each program includes:
✅ Complete code explanation
✅ Key concepts breakdown
✅ Step-by-step algorithm walkthrough
✅ Test URLs and expected outputs
✅ Essential takeaways for exam

## 🚀 Quick Navigation

### Concept-Based Learning Path
1. **Basics** (P3, P4, P5)
   - URL routing
   - String processing
   - Logic & conditionals

2. **Database** (P6, P7)
   - Models
   - Relationships
   - Admin interface

3. **Views & Templates** (P8)
   - Class-based views
   - Template rendering
   - Context passing

4. **Advanced** (P9, P10, P11)
   - File generation
   - AJAX basics
   - Real-time search

## 📝 Study Tips

1. **Read one program at a time** - Don't rush
2. **Copy the code** - Type it yourself for better learning
3. **Test locally** - Run the code and see output
4. **Modify and experiment** - Change parameters and observe
5. **Review takeaways** - Focus on key concepts before exam

## 🧪 Quick Test Commands

```powershell
# Activate environment
.\env\Scripts\Activate.ps1

# Navigate to project
cd myproject

# Run server
python manage.py runserver

# Access admin
# http://127.0.0.1:8000/admin/
```

## 📍 Exam Focus Areas

### Must Know
- [x] URL routing with parameters
- [x] Function-based views
- [x] Class-based views (ListView, DetailView)
- [x] Model definition and relationships
- [x] ORM queries (filter, get, all)
- [x] AJAX and JSON responses
- [x] Template rendering and variables

### Should Know
- [x] String processing and manipulation
- [x] Prime number algorithm
- [x] CSV and PDF generation
- [x] Form handling and validation
- [x] Dictionary operations
- [x] Exception handling

### Nice to Know
- [x] Admin customization
- [x] Django shell
- [x] Advanced ORM queries
- [x] Performance optimization

## 🎓 How to Use This Guide

1. **Before Exam**: Read and understand each program's concepts
2. **During Study**: Use quick reference section for definitions
3. **Last Minute**: Check the "Key Takeaways Summary" table
4. **Before Exam**: Review "Exam Quick Reference" section

## 💻 Interactive Learning

Best way to prepare:
1. Open this guide in one window
2. Open VS Code with code in another window
3. Run the project with `python manage.py runserver`
4. Test each URL while reading the guide
5. Modify code and observe changes

## ❓ Quick Definition Guide

| Term | Meaning |
|------|---------|
| **URL Pattern** | Django route definition like `path('cts/<int:s>/<int:n>')` |
| **View** | Python function that handles requests |
| **Model** | Database table representation |
| **Query** | Database search/filter operation |
| **AJAX** | Asynchronous request without page reload |
| **JSON** | Data format like `{"key": "value"}` |
| **Context** | Data passed to template `render(request, template, context)` |
| **ORM** | Object-Relational Mapping (Django models) |

## 📚 Quick Code Reference

### URL Routing
```python
path('cts/<int:s>/<int:n>', create_table_of_squares)
```

### View Function
```python
def view_name(request, param1, param2):
    return HttpResponse("response")
```

### Model
```python
class Student(models.Model):
    name = models.CharField(max_length=100)
```

### Query
```python
students = Student.objects.filter(name__icontains="John")
```

### AJAX
```javascript
$.ajax({ url: '/api/', success: function(data) {} })
```

---

## 🎓 Getting Started with Exam Prep

**Start here**: [Full Exam Preparation Guide →](myproject/EXAM_PREP.md)

---

**Last Updated**: March 30, 2026
**Format**: Exam Preparation Edition
**Scope**: Programs 3-11
