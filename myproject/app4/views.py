from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course
from .forms import StudentRegistrationForm, CourseSelectionForm


def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('select_course', student_id=student.id)
    else:
        form = StudentRegistrationForm()

    return render(request, 'app4/register_student.html', {'form': form})


def select_course(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = CourseSelectionForm(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']
            course.students.add(student)
            return redirect('course_students', course_id=course.id)
    else:
        form = CourseSelectionForm()

    return render(request, 'app4/select_course.html', {
        'form': form,
        'student': student
    })


def course_students(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    students = course.students.all()

    return render(request, 'app4/course_students.html', {
        'course': course,
        'students': students
    })