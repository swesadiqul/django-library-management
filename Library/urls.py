from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('adminclick/', adminclick, name="adminclick"),
    path('studentclick/', studentclick, name="studentclick"),
    path('admin_signup/', admin_signup, name="admin_signup"),
    path('admin_login/', admin_login, name="admin_login"),
    path('admin_profile/', admin_profile, name="admin_profile"),
    path('student_signup/', student_signup, name="student_signup"),
    path('student_login/', student_login, name="student_login"),
    path('student_profile/', student_profile, name="student_profile"),
    path('user_logout/', user_logout, name="user_logout"),
    path('about_us/', about_us, name="about_us"),
    path('contact_us/', contact_us, name="contact_us"),
    path('profile/', profile, name="profile"),
    path('add_book/', add_book, name="add_book"),
    path('view_book/', view_book, name="view_book"),
]
