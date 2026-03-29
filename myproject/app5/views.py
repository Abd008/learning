import csv
from django.http import HttpResponse, FileResponse
from app4.models import Student
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import ListView, DetailView


class StudentListView(ListView):
    model = Student
    template_name = 'app5/student_list.html'
    context_object_name = 'students'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'app5/student_detail.html'
    context_object_name = 'student'
def generate_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email'])

    students = Student.objects.all()
    for student in students:
        writer.writerow([student.first_name, student.last_name, student.email])

    return response
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