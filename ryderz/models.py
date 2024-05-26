from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Tutor(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=64)
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    birthday = models.DateField (editable=True)
    phone_number = models.IntegerField(null=True, blank=False)
    contact_method = models.CharField(max_length=256)
    university = models.CharField(max_length=256)
    availability = models.CharField(max_length=1024)
    picture = models.ImageField()
    resume = models.CharField(max_length = 1024)
    about_me = models.CharField(max_length = 1024)
    sex = models.CharField(null=True, max_length=32)
    subjects = models.ManyToManyField(Subject, blank=True, related_name="tutors")

    def __str__(self):
        return self.username

class Student(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=64)
    name = models.CharField(max_length=256)
    birthday = models.DateField(editable=True)
    phone_number = models.IntegerField(null=True, blank=False)
    contact_method = models.CharField(max_length=256)
    availability = models.CharField(max_length=1024)
    picture = models.ImageField(blank=True)
    about_me = models.CharField(max_length = 1024)
    sex = models.CharField(null=True, max_length=32)
    preferred_sex = models.CharField(null=True, max_length=32)     
    tutors = models.ManyToManyField(Tutor, blank=True, related_name="students")
    subjects = models.ManyToManyField(Subject, blank=True, related_name="students")

    def __str__(self):
        return self.username

class Request(models.Model):
    tutor = models.OneToOneField(Tutor, on_delete=models.CASCADE, related_name="request")
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="request")

class Review(models.Model):
    description = models.CharField(max_length=512)
    tutor = models.OneToOneField(Tutor, on_delete=models.CASCADE, related_name="review")
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="review")