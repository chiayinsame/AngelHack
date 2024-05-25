from django.shortcuts import render
from django import forms

class TeacherSignUpForm(forms.Form):
  CHOICES = [
    ('whatsapp', 'Whatsapp'),
    ('telegram', 'Telegram'),
    ('email', 'Email'),
    ('messages', 'Messages'),
  ]

  GENDERS = [
    ('male', 'Male'),
    ('female', 'Female'),
  ]

  username = forms.CharField(max_length=32, label="Username")
  password = forms.CharField(max_length=64, label="Password")
  name = forms.CharField(max_length=256, label="Full Name")
  email = forms.EmailField(max_length=256, label="Email") 
  sex = forms.ChoiceField(choices=GENDERS, label='Select Your Gender')
  birthday = forms.DateField(label="Date Of Birth")
  phone_number = forms.IntegerField(min_value=8, max_value=8, label="Phone Number")
  contact_method = forms.ChoiceField(choices=CHOICES, label='Select Preferred Contact Method')
  university = forms.CharField(max_length=256, label='Univeristy')
  availability = forms.CharField(max_length=256, label='Available Times')
  resume = forms.CharField(max_length=1024, label='Resume')
  about_me = forms.CharField(max_length=1024, label='About Me')
  picture = forms.ImageField()

def index(request):
  return render(request, "ryderz/index.html")

def tutor_signup(request):
  form = TeacherSignUpForm()
  return render(request, "ryderz/tutor_signup.html", {
    'form': form
  })

