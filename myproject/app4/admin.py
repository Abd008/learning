from django.contrib import admin
from .models import Student, Course


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    filter_horizontal = ('students',)


admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)