from django.views.generic import ListView, DetailView
from app4.models import Student


class StudentListView(ListView):
    model = Student
    template_name = 'app5/student_list.html'
    context_object_name = 'students'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'app5/student_detail.html'
    context_object_name = 'student'