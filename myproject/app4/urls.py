from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_student, name='register_student'),
    path('select/<int:student_id>/', views.select_course, name='select_course'),
    path('course/<int:course_id>/', views.course_students, name='course_students'),
]
