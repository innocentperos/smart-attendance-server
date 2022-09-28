from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields.related import ForeignKey
import datetime
import random
import string


# Create your models here.
USER_TYPES =(
    ('LECTURER','LECTURER'),
    ('STUDENT','STUDENT'),
    ("ADMIN", "ADMIN")
)

def convertDatetimeToString(o, dt = False):
    DATE_FORMAT = "%d %b , %Y" 
    TIME_FORMAT = "%H:%M:%S"
    if dt:
        return o.strftime("%s ; %s" % (DATE_FORMAT, TIME_FORMAT))

    if isinstance(o, datetime.date):
        return o.strftime(DATE_FORMAT)
    elif isinstance(o, datetime.time):
        return o.strftime(TIME_FORMAT)
    elif isinstance(o, datetime.datetime):
        return o.strftime("%s ; %s" % (DATE_FORMAT, TIME_FORMAT))


def random_id(size=12, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class UserType ( models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user.username} - {self.user_type}'

class XSession (models.Model):
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE )
    session = models.CharField(max_length=100)
    expires = models.DateTimeField(default=datetime.datetime.now)

class Lecturer (models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    email = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.email}'

class Course(models.Model):
    title = models.CharField(max_length=120)
    code =  models.CharField(max_length=120)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)

    def attendances(self):
        queries = Attendance.objects.filter(course = self)
        return len(queries)

    def __str__(self):
        return f' {self.title} For {str(self.lecturer)} '
class Attendance(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)
    lat = models.CharField(max_length=100)
    long = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    is_open = models.BooleanField(default=True)
    commit = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.date()} {str(self.course)} ({self.code})"

    def attendances(self):
        attendances = StudentAttendance.objects.filter(attendance = self).count()

        return attendances
    
    def date(self):
        return convertDatetimeToString(self.datetime, True)
    
    def course_title(self):
        return self.course.title
    def course_code(self):
        return self.course.code
        
class Student(models.Model):
    matric_number = models.CharField(max_length=100)
    image = models.FileField(max_length=200, upload_to="students_images")

    def __str__(self):
        return f"{self.matric_number}"

class StudentAttendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    lat = models.CharField(max_length=100, null=True)
    long = models.CharField(max_length=100, null=True)
    score = models.IntegerField( default=-1)
    distance = models.FloatField(default=-1, null=True)
    attendance_image = models.FileField(max_length=250, upload_to="attendance_image")
    commit = models.BooleanField(default=False)
    datetime = models.DateTimeField( auto_created=True,null=True)

    def __str__(self):
        return f"{str(self.attendance)} / {str(self.student)} "

    def matric_number (self):
        return self.student.matric_number

    def date(self):
        return convertDatetimeToString(self.datetime, True)