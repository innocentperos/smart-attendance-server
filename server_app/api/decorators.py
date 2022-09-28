from functools import wraps
from rest_framework.request import Request
from django.http.request import HttpRequest as Request2
from rest_framework import exceptions

from server_app.models import Lecturer


def lecturer_only(function):
    
    @wraps(function)
    def wrap(*args, **kwargs):

        request = None
        for req in args:
            if isinstance(req,(Request, Request2)):
                request = req
                break
        if not request:
            raise exceptions.AuthenticationFailed("something wrong")

        if not request.user:
            raise exceptions.NotAuthenticated("Please login first")
        
        try:
            lecturer = Lecturer.objects.get(user = request.user)

            request.lecturer = lecturer

            return function(*args, **kwargs)
        except Lecturer.DoesNotExist:
            raise exceptions.AuthenticationFailed("Please login as a lecturer, to access this")
        
    return wrap


