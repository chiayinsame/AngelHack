from django.shortcuts import render
from django import forms
from .models import Tutor, Student, Subject

class SignInForm(forms.Form):
  username = forms.CharField(max_length=32, label="Username")
  password = forms.CharField(max_length=64, label="Password")
  type = forms.CharField(widget=forms.HiddenInput(), initial='none')

class TeacherSignUpForm(forms.ModelForm):
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
    birthday = forms.DateField(label="Date Of Birth", widget=forms.DateInput(attrs={'type': 'date'}))
    phone_number = forms.IntegerField(min_value=80000000, max_value=99999999, label="Phone Number")
    contact_method = forms.ChoiceField(choices=CHOICES, label='Select Preferred Contact Method')
    university = forms.CharField(max_length=256, label='University')
    availability = forms.CharField(max_length=1024, label='Availability (Date and Time)')
    resume = forms.CharField(max_length=1024, label='Resume', widget=forms.Textarea)
    about_me = forms.CharField(max_length=1024, label='About Me', widget=forms.Textarea)
    picture = forms.ImageField(required=False)
    subjects = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), widget=forms.CheckboxSelectMultiple, label='Subjects')

    class Meta:
        model = Tutor
        fields = [
            'username', 'password', 'name', 'email', 'sex', 'birthday', 'phone_number', 'contact_method',
            'university', 'availability', 'resume', 'about_me', 'picture', 'subjects'
        ]

def index(request):
  form = SignInForm()
  return render(request, "ryderz/index.html", {
    'form': form
  })

def tutor_signup(request):
      if request.method == 'POST':
        form = TeacherSignUpForm(request.POST, request.FILES)
        if form.is_valid():
          tutor = form.save()
          return render(request, "ryderz/tutor_profile.html", {
            'tutor': tutor,
            'username': tutor.username,
            'name': tutor.name,
            'birthday': tutor.birthday,
            'email': tutor.email,
            'phone_number': tutor.phone_number,
            'contact_method': tutor.contact_method,
            'university': tutor.university,
            'availability': tutor.availability,
            'picture': tutor.picture,
            'resume': tutor.resume,
            'about_me': tutor.about_me,
            'sex': tutor.sex
          })
      else:
        form = TeacherSignUpForm()
        return render(request, "ryderz/tutor_signup.html", {
          'form': form
        })

def signup(request):
  return render(request, "ryderz/signup.html")