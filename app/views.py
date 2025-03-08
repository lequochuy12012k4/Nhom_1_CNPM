from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import *
from .models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

def home(request):
    if request.user.is_authenticated:
        user_not_login = "hidden"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "hidden"
    context = {'user_not_login':user_not_login,'user_login':user_login}
    return render(request,'app/home.html',context)

def user(request):
    return render(request,'app/user.html')

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
    context = {'user_not_login':user_not_login,'user_login':user_login}
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

def Tien_trinh(request):
    if request.user.is_authenticated:
        user_not_login = "hidden"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "hidden"
    context = {'user_not_login':user_not_login,'user_login':user_login}
    return render(request,'app/user/tien_trinh.html',context)

def Vinh_danh(request):
    if request.user.is_authenticated:
        user_not_login = "hidden"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "hidden"
    rankings = [
        {'rank': 1, 'username': 'JohnDoe', 'score': 1000},
        {'rank': 2, 'username': 'JaneSmith', 'score': 950},
        {'rank': 4, 'username': 'PeterJones', 'score': 900},
        {'rank': 5, 'username': 'PeterJones', 'score': 900},
        {'rank': 6, 'username': 'PeterJones', 'score': 900},
        {'rank': 7, 'username': 'PeterJones', 'score': 900},
        {'rank': 8, 'username': 'PeterJones', 'score': 900},
        {'rank': 9, 'username': 'PeterJones', 'score': 900},
        {'rank': 10, 'username': 'PeterJones', 'score': 900},
        {'rank': 11, 'username': 'PeterJones', 'score': 900},
        {'rank': 12, 'username': 'PeterJones', 'score': 900},
        {'rank': 13, 'username': 'PeterJones', 'score': 900},
        {'rank': 14, 'username': 'PeterJones', 'score': 900},
        {'rank': 15, 'username': 'PeterJones', 'score': 900},
    ]
    context = {'user_not_login':user_not_login,'user_login':user_login, 'rankings': rankings}
    return render(request,'app/vinh_danh.html', context)
