from django.contrib import admin
from django.contrib import messages
from django.urls import path
from django.shortcuts import render
from .models import *
from django import forms
from .models import Login_User
from django.http import HttpResponseRedirect
from django.urls import reverse
# Register your models here.
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

admin.site.register(customer)
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Chatbot_message)