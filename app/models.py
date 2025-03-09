from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms  
from django.forms.widgets import PasswordInput, TextInput
# Create your models here.

class Category(models.Model):
    sub_category = models.ForeignKey('self',on_delete=models.CASCADE, related_name='sub_categories',null=True, blank=True)    
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    def __str__(self):
        return self.name
    
class Course(models.Model):
    category = models.ManyToManyField(Category,related_name="course")
    name  = models.CharField(max_length=200,null=True)
    price = models.FloatField()

    def __str__(self):
        return self.name
    
class Login_User(models.Model):
    username = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.username
    
class customer(models.Model):
  username = models.CharField(max_length=50, null=True)
  password = models.CharField(max_length=200, null=True)

  def __str__(self):
    return self.username

class CreateLoginForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Tên đăng nhập'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Mật khẩu'}))
    
#Change form register
class CreateRegisterForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mật khẩu'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Xác nhận mật khẩu'}))
    phone_number = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập số điện thoại'}))
    class Meta:
        model = User
        fields = ['first_name','last_name','username','phone_number','email', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={
                        'class':'form-control',
                        'placeholder':'Họ',
                }), 
            'last_name': forms.TextInput(attrs={
                        'class':'form-control',
                        'placeholder':'Tên',
                }), 
            'username': forms.TextInput(attrs={
                        'class':'form-control',
                        'placeholder':'Tên đăng nhập',
                }), 
            'email': forms.EmailInput(attrs={
                        'class':'form-control',
                        'placeholder':'Email',
                }),

        }