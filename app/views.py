from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse

def home(request):
    if request.user.is_authenticated:
        user_not_login = "hidden"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "hidden"
    context = {'user_not_login':user_not_login,'user_login':user_login}
    return render(request,'app/home.html',context)

def Cap_nhat_thong_tinPage(request):
    form = EditProfile(request.POST, instance=request.user)
    if request.method == "POST":
        user_not_login = "hidden"
        user_login = "show"
        context = {
            'user': request.user,
            'user_not_login':user_not_login,
            'user_login':user_login,
            'form' : form
        }
        if form.is_valid():
            form.save()
            return render(request,'app/user/thong_tin.html',context)
    else:
        user_not_login = "show"
        user_login = "hidden"
        context = {
            'user': request.user,
            'user_not_login':user_login,
            'user_login':user_not_login,
            'form' : form
        }
        return render(request,'app/user/cap_nhat_thong_tin.html',context)

def Thay_doi_mat_khauPage(request):
    form = ChangePassword(data = request.POST, user=request.user)
    if request.method == "POST":
        user_not_login = "hidden"
        user_login = "show"
        context = {
            'user': request.user,
            'user_not_login':user_not_login,
            'user_login':user_login,
            'form' : form
        }
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return render(request,'app/user/thong_tin.html',context)
    else:
        user_not_login = "show"
        user_login = "hidden"
        context = {
            'user': request.user,
            'user_not_login':user_login,
            'user_login':user_not_login,
            'form' : form
        }
        return render(request,'app/user/thay_doi_mat_khau.html',context)

def RegisterPage(request):
    form = CreateRegisterForm()
    context = {'form' : form}
    if request.method == "POST":
        form = CreateRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'app/register.html',context)

def LoginPage(request):
    form = CreateLoginForm()
    context = {'loginform': form}
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request,"Tên đăng nhập hoặc mật khẩu chưa chính xác")
    return render(request, 'app/login.html', context)

def logoutPage(request):
    logout(request)
    response = redirect('home')
    return response

#Link to "Lộ trình"

def Lo_trinhPage(request):
    return render(request,'app/lo_trinh.html')

#Link to "Lịch khai giảng"
def Lich_khai_giangPage(request):
    if request.user.is_authenticated:
        user_not_login = "hidden"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "hidden"
    context = {'user_not_login':user_not_login,'user_login':user_login}
    return render(request,'app/lich_khai_giang.html',context)

#Link to "Flash_card"
import os
from django.conf import settings
from django.shortcuts import render
from django import forms

class AddWordForm(forms.Form):
    new_word = forms.CharField(label="Từ mới")
    new_meaning = forms.CharField(label="Nghĩa")
    new_example = forms.CharField(label="Ví dụ", widget=forms.Textarea)

def Flash_CardPage(request):
    if request.user.is_authenticated:
        user_not_login = "hidden"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "hidden"

    file = open(os.path.join(settings.BASE_DIR, 'app\\static\\app\\data\\Book2.csv'),encoding='utf-8-sig')
    key = file.readline().strip()
    keys = key.split(",")

    value = file.readline().strip()
    data_word = []
    while value!="":
        index = 0
        values = value.split(",")
        index_data = {}
        for index in range(len(keys)):
            if keys[index] == 'id':
                values[index] = int(values[index])

            my_dict = {keys[index]:values[index]}
            index_data.update(my_dict)
        data_word.append(index_data)
        value = file.readline().strip()

    if request.method == 'POST':
        form = AddWordForm(request.POST)
        if form.is_valid():
            new_word = form.cleaned_data['new_word']
            new_meaning = form.cleaned_data['new_meaning']
            new_example = form.cleaned_data['new_example']

            # Add the new word to the data_word list (in-memory only)
            data_word.append({'word': new_word, 'meaning': new_meaning, 'example': new_example})

            # Re-initialize the form
            form = AddWordForm()
    else:
        form = AddWordForm()  # Create a blank form instance

    context = {'user_not_login': user_not_login, 'user_login': user_login, 'data_word':data_word, 'form':form}
    return render(request,'app/flash_card.html',context)

#Link to "Khóa học"
def Khoa_hoc(request):
    if request.user.is_authenticated:
        user_not_login = "hidden"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "hidden"
    context = {'user_not_login':user_not_login,'user_login':user_login}
    return render(request,'app/course.html',context)

def ToiecPage(request):
    if request.user.is_authenticated:
        user_not_login = "hidden"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "hidden"
    context = {'user_not_login':user_not_login,'user_login':user_login}
    return render(request,'app/khoa_hoc/TOEIC.html',context)

def IeltsPage(request):
    if request.user.is_authenticated:
        user_not_login = "hidden"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "hidden"
    context = {'user_not_login':user_not_login,'user_login':user_login}
    return render(request,'app/khoa_hoc/IELTS.html',context)

def THPTQGPage(request):
    if request.user.is_authenticated:
        user_not_login = "hidden"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "hidden"
    context = {'user_not_login':user_not_login,'user_login':user_login}
    return render(request,'app/khoa_hoc/THPTQG.html',context)

#Link to "Giáo viên"
def Gioi_thieuPage(request):
    if request.user.is_authenticated:
        user_not_login = "hidden"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "hidden"
    context = {'user_not_login':user_not_login,'user_login':user_login}
    return render(request,'app/gioi_thieu.html',context)

#Link to "Test Online":
def Test_onlinePage(request):
    if request.user.is_authenticated:
        user_not_login = "hidden"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "hidden"
    context = {'user_not_login':user_not_login,'user_login':user_login}
    return render(request,'app/test_online.html',context)

#Link to "Username"
def Thong_tin(request):
    if request.user.is_authenticated:
        user_not_login = "hidden"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "hidden"
    context = {
        'user_not_login':user_not_login,
        'user_login':user_login
    }
    return render(request,'app/user/thong_tin.html',context)

def Thanh_toan(request):
    if request.user.is_authenticated:
        user_not_login = "hidden"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "hidden"
    context = {'user_not_login':user_not_login,'user_login':user_login}
    return render(request,'app/user/thanh_toan.html',context)

import os
from django.conf import settings
def Vinh_danh(request):
    if request.user.is_authenticated:
        user_not_login = "hidden"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "hidden"

    file = open(os.path.join(settings.BASE_DIR, 'app\\static\\app\\data\\Book1.csv'),encoding='utf-8-sig')
    key = file.readline().strip()
    keys = key.split(",")

    value = file.readline().strip()
    data_rankings = []
    while value!="":
        index = 0
        values = value.split(",")
        index_data = {}
        for index in range(len(keys)):
            if keys[index] == 'score' or keys[index] == 'rank':
                values[index] = int(values[index])
            
            my_dict = {keys[index]:values[index]}
            index_data.update(my_dict)   
        data_rankings.append(index_data)
        value = file.readline().strip()
    context = {'user_not_login':user_not_login,'user_login':user_login, 'data_ranking': data_rankings}
    return render(request,'app/vinh_danh.html', context)
