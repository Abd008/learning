from django.urls import path
from .views import StudentListView, StudentDetailView
from .views import generate_csv, generate_pdf

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('students/csv/', generate_csv, name='generate_csv'),
    path('students/pdf/', generate_pdf, name='generate_pdf'),
]

