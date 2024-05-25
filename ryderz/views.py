from django.shortcuts import render
from django import forms

class SignInForm(forms.Form):
  username = forms.CharField(max_length=32, label="Username")
  password = forms.CharField(max_length=64, label="Password")
  type = forms.CharField(widget=forms.HiddenInput(), initial='none')

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
  phone_number = forms.IntegerField(min_value=80000000, max_value=99999999, label="Phone Number")
  contact_method = forms.ChoiceField(choices=CHOICES, label='Select Preferred Contact Method')
  university = forms.CharField(max_length=256, label='University')
  availability = forms.CharField(max_length=256, label='Availability (Date and Time)')
  resume = forms.CharField(max_length=1024, label='Resume')
  about_me = forms.CharField(max_length=1024, label='About Me')
  picture = forms.ImageField()

def index(request):
  form = SignInForm()
  return render(request, "ryderz/index.html", {
    'form': form
  })

def tutor_signup(request):
  form = TeacherSignUpForm()
  return render(request, "ryderz/tutor_signup.html", {
    'form': form
  })

def signup(request):
  return render(request, "ryderz/signup.html")