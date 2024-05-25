from django.contrib import admin
from .models import Subject, Tutor, Student, Request, Review

admin.site.register(Subject)
admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(Request)
admin.site.register(Review)