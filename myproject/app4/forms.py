from django import forms
from .models import Student, Course

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email']


class CourseSelectionForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all())