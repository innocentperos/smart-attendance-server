from django.db.models import fields
from rest_framework import serializers


from server_app.models import Attendance, Course, Lecturer,StudentAttendance


class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    lecturer = LecturerSerializer()

    class Meta:
        model = Course
        fields = ['id','title','code','lecturer','attendances']

class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = ['id','course','date','datetime','lat','long','code','is_open','commit','attendances','course_title','course_code']


class StudentAttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentAttendance
        fields = ['id',
        'attendance',
        'datetime',
        'lat'
        ,'long',
        'commit',
        'matric_number',
        'attendance_image',
        'date']

    