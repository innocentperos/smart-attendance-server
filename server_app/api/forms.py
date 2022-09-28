from django import forms
from django.forms import fields

from server_app.models import Attendance, Course, Student

class LoginForm(forms.Form):

    email = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)

class CourseForm( forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title','code']

class AttendanceForm (forms.ModelForm):

    class Meta:
        model = Attendance
        fields = ['course', 'lat', 'long']

class StudentForm( forms.ModelForm):
    class Meta:
        model = Student
        fields = ['matric_number', 'image']
        