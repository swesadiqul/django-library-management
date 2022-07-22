from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

class AdminProfile(models.Model):
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=100, choices=gender_choices)
    # image = models.ImageField(default="default.png", upload_to='library/images')

    def __str__(self):
        return self.user.username

    # def save(self):
    #     super().save()
    #     img = Image.open(self.image.path)
    #     if img.height > 200 or img.width > 200:
    #         output_size = (200, 200)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

# class StudentProfile(models.Model):
#     gender_choices = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Others'),
#     )
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     date_of_birth = models.DateField()
#     gender = models.CharField(max_length=100, choices=gender_choices)
#     image = models.ImageField(upload_to='images/')



class AddBook(models.Model):
    name = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=255)


    def __str__(self):
        return self.name

# class IssueNewBook(models.Model):
