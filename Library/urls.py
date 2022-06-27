from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('adminclick/', adminclick, name="adminclick"),
    path('studentclick/', studentclick, name="studentclick"),
    path('admin_registration/', admin_registration, name="admin_registration"),
    path('student_registration/', student_registration, name="student_registration"),
]
