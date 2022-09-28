from django.contrib import admin
from server_app.models import Attendance, Course, Lecturer, Student, StudentAttendance, UserType, XSession
# Register your models here.

admin.site.register(Lecturer)
admin.site.register(Course)
admin.site.register(UserType)
admin.site.register(XSession)
admin.site.register(Attendance)
admin.site.register(Student)
admin.site.register(StudentAttendance)
