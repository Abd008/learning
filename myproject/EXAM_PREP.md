# Django Lab Manual - Exam Preparation Guide

A focused study guide covering essential concepts from Programs 3-11 for exam preparation.

---

## 📚 Program 3: Table of Squares

**Question**: Develop a Django application that displays tables of squares of pairs of numbers input through the URL.

### Key Concepts

#### 1. **URL Routing with Path Parameters**
```python
# In myproject/urls.py
from app1.views import create_table_of_squares

urlpatterns = [
    path('cts/<int:s>/<int:n>', create_table_of_squares),
]
```

**How it works:**
- `<int:s>` - Captures first integer parameter (starting number)
- `<int:n>` - Captures second integer parameter (number of iterations)
- `/cts/2/5` → s=2, n=5

#### 2. **Function-Based Views**
```python
# In app1/views.py
from django.http import HttpResponse

def create_table_of_squares(request, s, n):
    result = ""
    for i in range(1, n+1):
        result += f"<p>{s} * {i} = {s*i}</p>"
    return HttpResponse(result)
```

**Components:**
- `request` - Django request object (always first parameter)
- `s`, `n` - URL parameters captured from path
- `range(1, n+1)` - Loop from 1 to n (inclusive)
- `HttpResponse()` - Return HTML as HTTP response

#### 3. **String Building in Loop**
```python
result = ""
for i in range(1, n+1):
    result += f"<p>{s} * {i} = {s*i}</p>"
```

- Concatenate strings in loop
- f-string for formatting: `f"text {variable}"`
- Build HTML incrementally

### Test URL
```
http://127.0.0.1:8000/cts/2/5
```

**Output:**
```
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
```

### Essential Takeaways
✓ URL parameters: `<type:name>`
✓ View function receives parameters
✓ Return `HttpResponse()` with HTML
✓ Use loops and formatting for dynamic content

---

## 📚 Program 4: Vowels & Consonants Counter

**Question**: Develop a Django application that displays the number of vowels and consonants and also lists them for any input sentence specified in the URL.

### Key Concepts

#### 1. **URL Routing with String Parameters**
```python
# In myproject/urls.py
path('vc/<str:sentence>/', vc),
```

**How it works:**
- `<str:sentence>` - Captures string parameter
- `/vc/hello%20world/` → sentence="hello world"
- URL-encoded spaces: `%20` represents space

#### 2. **String Processing & Character Classification**
```python
def vc(request, sentence):
    vow_cnt = 0
    cons_cnt = 0
    vow_dict = {}
    cons_dict = {}

    for letter in sentence:
        if letter.isalpha():  # Check if alphabetic
            if letter.lower() in "aeiou":  # Vowel check
                vow_cnt += 1
                vow_dict[letter] = vow_dict.get(letter, 0) + 1
            else:  # Consonant
                cons_cnt += 1
                cons_dict[letter] = cons_dict.get(letter, 0) + 1
```

**Key Methods:**
- `letter.isalpha()` - Returns True if alphabetic character
- `letter.lower()` - Convert to lowercase
- `letter in "aeiou"` - Check if vowel
- `.get(key, default)` - Dictionary get with default value

#### 3. **Dictionary Frequency Counting**
```python
vow_dict[letter] = vow_dict.get(letter, 0) + 1
```

**Logic:**
- If letter exists: increment count
- If letter doesn't exist: start at 0, then increment to 1
- Example: 'h' appears 1 time, 'e' appears 2 times

#### 4. **Iterating Dictionary Items**
```python
for key, value in vow_dict.items():
    result += f"<p>{key}: {value}</p>"
```

- `.items()` returns (key, value) pairs
- Iterate through each letter and its count

### Test URL
```
http://127.0.0.1:8000/vc/hello/
```

**Output:**
```
3 Vowels and 2 Consonants

Vowel Counter
e: 1
o: 1

Consonant Counter
h: 1
l: 2
```

### Essential Takeaways
✓ Character classification: `isalpha()`, `in` operator
✓ Vowel/consonant detection
✓ Dictionary for counting frequencies
✓ `.get()` method for safe dictionary access
✓ `.items()` for iterating dictionaries

---

## 📚 Program 5: Prime Number Checker

**Question**: Develop a Django project to check whether a given number is prime or not.

### Key Concepts

#### 1. **Prime Number Logic**
```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```

**Algorithm Explanation:**
- `n <= 1`: Not prime
- `n <= 3`: Primes (2, 3)
- `n % 2 == 0 or n % 3 == 0`: Divisible by 2 or 3? Not prime
- `while i * i <= n`: Check divisors up to √n
- Check `i` and `i+2` (optimization for 6k±1 form)

#### 2. **Form-Based Input**
```python
def home(request):
    result = None
    number = None

    if request.method == 'POST':
        number = request.POST.get('number')
        try:
            number = int(number)
            result = is_prime(number)
        except:
            result = "Invalid input"

    return render(request, 'app3/home.html', {
        'result': result,
        'number': number
    })
```

**HTTP Methods:**
- `request.method == 'POST'` - Check if form submitted
- `request.POST.get('number')` - Get form field value
- `try/except` - Handle invalid input

#### 3. **Template Rendering with Context**
```python
return render(request, 'app3/home.html', {
    'result': result,
    'number': number
})
```

**Context Dictionary:**
- Pass data to template
- Variables available in template: `{{ result }}`, `{{ number }}`

### Essential Takeaways
✓ Prime checking algorithm
✓ HTTP POST method handling
✓ Form data retrieval: `.POST.get()`
✓ Exception handling: `try/except`
✓ Template context passing

---

## 📚 Program 6 & 7: Student-Course Models & Admin

**Question**: Develop a Django application that performs student registration to a course with admin interface.

### Key Concepts

#### 1. **Model Definition with ManyToMany**
```python
# In app4/models.py
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    students = models.ManyToManyField(Student, related_name='courses')

    def __str__(self):
        return self.name
```

**Field Types:**
- `CharField(max_length=50)` - String with max length
- `EmailField(unique=True)` - Email with uniqueness
- `TextField()` - Longer text
- `ManyToManyField()` - Many-to-many relationship

#### 2. **Registering Models in Admin**
```python
# In app4/admin.py
from django.contrib import admin
from .models import Student, Course

admin.site.register(Student)
admin.site.register(Course)
```

#### 3. **Access Admin**
```
http://127.0.0.1:8000/admin/
```

**Admin Features:**
- Create, Read, Update, Delete (CRUD)
- Manage many-to-many relationships
- Filter and search

### Essential Takeaways
✓ Model field types
✓ ManyToMany relationships
✓ Unique constraints
✓ `__str__()` method for object representation
✓ Admin registration

---

## 📚 Program 8: Class-Based Views

**Question**: Create generic class-based views that display a list of students and a detailed view for any selected student.

### Key Concepts

#### 1. **ListView - Display All Items**
```python
from django.views.generic import ListView
from app4.models import Student

class StudentListView(ListView):
    model = Student
    template_name = 'app5/student_list.html'
    context_object_name = 'students'
```

**Attributes:**
- `model` - Model to query (Student.objects.all())
- `template_name` - Template file to render
- `context_object_name` - Variable name in template

**Template Usage:**
```html
{% for student in students %}
    <p>{{ student.first_name }} - {{ student.email }}</p>
{% endfor %}
```

#### 2. **DetailView - Display Single Item**
```python
from django.views.generic import DetailView

class StudentDetailView(DetailView):
    model = Student
    template_name = 'app5/student_detail.html'
    context_object_name = 'student'  # SINGULAR
```

**Important:** context_object_name should be singular for DetailView

**URL Pattern:**
```python
path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail')
```

**Template Usage:**
```html
<p>Name: {{ student.first_name }} {{ student.last_name }}</p>
<p>Email: {{ student.email }}</p>
```

#### 3. **Key Differences**
| Feature | ListView | DetailView |
|---------|----------|-----------|
| Purpose | Multiple items | Single item |
| URL | `/students/` | `/students/5/` |
| Default query | `.all()` | `.get(pk=id)` |
| Context var | Plural | Singular |
| `.as_view()` | Required | Required |

### Essential Takeaways
✓ ListView for list of objects
✓ DetailView for single object
✓ Generic class-based views simplify code
✓ Template naming conventions
✓ Context object names (plural vs singular)

---

## 📚 Program 9: CSV & PDF Generation

**Question**: Develop a Django application that performs CSV and PDF generation for models.

### Key Concepts

#### 1. **CSV Generation**
```python
def generate_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email'])

    students = Student.objects.all()
    for student in students:
        writer.writerow([student.first_name, student.last_name, student.email])

    return response
```

**Key Components:**
- `content_type='text/csv'` - File type
- `Content-Disposition` - Download as attachment
- `csv.writer()` - CSV file writer
- `writerow()` - Write single row
- Query database and iterate

#### 2. **PDF Generation**
```python
from reportlab.pdfgen import canvas
from io import BytesIO
from django.http import FileResponse

def generate_pdf(request):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    students = Student.objects.all()

    y = 800
    for student in students:
        text = f"{student.first_name} {student.last_name} - {student.email}"
        p.drawString(50, y, text)
        y -= 20

    p.save()
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename='students.pdf')
```

**Key Components:**
- `BytesIO()` - In-memory file
- `canvas.Canvas()` - PDF canvas
- `drawString(x, y, text)` - Draw text at coordinates
- `p.save()` - Save to buffer
- `FileResponse()` - Return file for download

### URLs
```python
path('students/csv/', generate_csv, name='generate_csv'),
path('students/pdf/', generate_pdf, name='generate_pdf'),
```

### Essential Takeaways
✓ CSV file generation with `csv.writer`
✓ PDF generation with ReportLab
✓ HTTP response headers for downloads
✓ File attachments and downloads
✓ In-memory file handling

---

## 📚 Program 10: AJAX Student Registration

**Question**: Develop a registration page for student enrollment without page refresh using AJAX.

### Key Concepts

#### 1. **AJAX Form Submission**
```javascript
$('#student-form').on('submit', function(e) {
    e.preventDefault();  // Prevent page reload
    
    $.ajax({
        type: 'POST',
        url: "{% url 'ajax_student' %}",
        data: $(this).serialize(),
        success: function(response) {
            if (response.success) {
                alert('Student registered!');
                $('#student-form')[0].reset();
            }
        }
    });
});
```

**Key Methods:**
- `e.preventDefault()` - Stop form default submission
- `$.ajax()` - Asynchronous request
- `$(this).serialize()` - Convert form to query string
- `success` callback - Handle response

#### 2. **Backend AJAX Handler**
```python
def ajax_student(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        
        # Validation
        if not all([first_name, last_name, email]):
            return JsonResponse({
                'success': False, 
                'message': 'All fields required'
            })
        
        # Check email uniqueness
        if Student.objects.filter(email=email).exists():
            return JsonResponse({
                'success': False, 
                'message': 'Email already registered'
            })
        
        # Create student
        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        
        return JsonResponse({
            'success': True, 
            'message': f'Student {student.first_name} registered',
            'student_id': student.id
        })
```

**Key Points:**
- `request.POST.get()` - Get form data
- `.strip()` - Remove whitespace
- Validation before saving
- `Student.objects.filter().exists()` - Check uniqueness
- `JsonResponse()` - Return JSON

#### 3. **JSON Response Format**
```json
{
    "success": true,
    "message": "Student registered successfully",
    "student_id": 5
}
```

### Essential Takeaways
✓ AJAX for asynchronous requests
✓ `prevent Default()` to stop page reload
✓ `JsonResponse` for API responses
✓ Form validation and error handling
✓ Input sanitization with `.strip()`

---

## 📚 Program 11: AJAX Course Search

**Question**: Develop a search application in Django using AJAX that displays courses enrolled by a student being searched.

### Key Concepts

#### 1. **Real-Time Search with AJAX**
```javascript
$('#search-box').on('keyup', function() {
    var query = $(this).val();

    if (query.length < 2) {
        $('#results').html('');
        return;
    }

    $.ajax({
        url: "{% url 'search_students' %}",
        data: { 'query': query },
        success: function(response) {
            var output = "";

            response.results.forEach(function(student) {
                output += "<div>";
                output += "<b>" + student.name + "</b><br>";
                output += "Courses: " + student.courses.join(", ");
                output += "</div>";
            });

            $('#results').html(output);
        }
    });
});
```

**Events & Methods:**
- `.on('keyup')` - Trigger on every keystroke
- `.val()` - Get input value
- `.length < 2` - Minimum 2 characters
- `forEach()` - Iterate array
- `.join(", ")` - Convert array to string
- `.html()` - Set content

#### 2. **Backend Search Handler**
```python
def search_students(request):
    query = request.GET.get('query', '').strip()

    if not query or len(query) < 2:
        return JsonResponse({'results': []})

    students = Student.objects.filter(
        first_name__icontains=query
    ) | Student.objects.filter(
        last_name__icontains=query
    )

    results = []
    for student in students:
        course_list = [course.name for course in student.courses.all()]
        results.append({
            'id': student.id,
            'name': f"{student.first_name} {student.last_name}",
            'email': student.email,
            'courses': course_list if course_list else ['No courses']
        })

    return JsonResponse({'results': results})
```

**Database Queries:**
- `__icontains` - Case-insensitive contains
- `|` operator - OR condition
- `.all()` - Get all related objects
- List comprehension - `[course.name for course ...]`

#### 3. **JSON Response Format**
```json
{
    "results": [
        {
            "id": 1,
            "name": "John Doe",
            "email": "john@example.com",
            "courses": ["Python", "Django"]
        }
    ]
}
```

### Essential Takeaways
✓ Keyup event for live search
✓ Minimum character check
✓ Case-insensitive database queries
✓ OR queries with `|` operator
✓ Related object retrieval
✓ Array iteration and manipulation

---

## 🎯 Exam Quick Reference

### HTTP Methods
- **GET**: Retrieve data (URL parameters, safe)
- **POST**: Submit data (form data, hidden)

### URL Patterns
```python
path('cts/<int:s>/<int:n>', view_name)        # Integer parameters
path('vc/<str:sentence>/', view_name)         # String parameters
path('students/<int:pk>/', StudentDetailView) # Primary key
```

### Response Types
- **HttpResponse()** - Plain text/HTML
- **JsonResponse()** - JSON data
- **FileResponse()** - File download
- **render()** - Template rendering

### Django ORM Queries
```python
Student.objects.all()                    # All students
Student.objects.filter(email=x)          # Filtered query
Student.objects.filter(first_name__icontains=x)  # Case-insensitive
Student.objects.get(pk=1)                # Single object
student.courses.all()                    # Related objects
```

### Template Tags
```django
{% for item in items %}
    {{ item.field }}
{% endfor %}

{{ variable }}               # Variable interpolation
{% url 'name' %}            # URL reverse lookup
```

### JavaScript AJAX
```javascript
$.ajax({
    url: '/endpoint/',
    data: { key: value },
    success: function(response) { }
})
```

### Common Decorators
```python
@require_http_methods(["GET"])         # Restrict HTTP method
```

---

## 💡 Important Study Tips

1. **URL Routing**: Always check path configuration in both app and project urls.py
2. **View Parameters**: URL parameters must match view function parameters
3. **Context Variables**: Template variable names depend on view configuration
4. **ManyToMany**: Always use `related_name` for reverse access
5. **AJAX**: Always prevent form default with `preventDefault()`
6. **Validation**: Always validate and sanitize user input
7. **Database Queries**: Use `__icontains` for case-insensitive search
8. **JSON Response**: Ensure proper response structure in AJAX handlers

---

## ✅ Key Takeaways Summary

| Concept | Key Point |
|---------|-----------|
| **URL Parameters** | `<type:name>` syntax, captured by view |
| **Views** | Function-based or class-based |
| **Models** | Define fields and relationships |
| **Admin** | CRUD interface for models |
| **Templates** | Display data with template tags |
| **AJAX** | Asynchronous requests, JSON responses |
| **Forms** | POST method, validation, error handling |
| **Queries** | Filter, get, all, related objects |
| **Response Types** | HttpResponse, JsonResponse, FileResponse, render |

---

**Last Updated**: March 30, 2026
**Version**: 1.0 (Exam Prep Edition)
