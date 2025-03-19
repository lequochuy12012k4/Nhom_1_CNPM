from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

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

def LogoutPage(request):
    logout(request)
    response = redirect('home')
    return response

#Link to "Lộ trình"

def Lo_trinhPage(request):
    return render(request,'app/lo_trinh.html')

#Link to "Lịch khai giảng"
def Tai_lieuPage(request):
    if request.user.is_authenticated:
        user_not_login = "hidden"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "hidden"
    context = {'user_not_login':user_not_login,'user_login':user_login}
    return render(request,'app/tai_lieu.html',context)

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
    file_name = 'vocalbulary.csv'
    file = open(os.path.join(settings.BASE_DIR, f'app\\static\\app\\data\\{file_name}'),encoding='utf-8-sig')
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

def FlashCardTuhocPage(request):

    if request.user.is_authenticated:
        user_not_login = "hidden"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "hidden"
    context = {'user_not_login':user_not_login,'user_login':user_login}
    return render(request,'app/flash_card_tu_hoc.html',context)

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
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import numpy as np
def Thong_tin(request):
    #Thống kê số điểm
    # 1. Data Preparation
    x_labels = ["0-300+", "450-600+", "730+"]
    x = np.array([1, 2, 3])  # Numerical values for X-axis positions
    y = np.array([250, 600, 750]) # Corresponding numerical values for each x

    # 2. Create the Plot (Epic Styling!)
    plt.figure(figsize=(12, 8), facecolor="#222222")
    ax = plt.axes()
    ax.set_facecolor("#333333")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    plt.plot(x, y, color="#00FFFF", linewidth=2, marker='o', markersize=8)  # Plot the data
    plt.xlabel("Khóa học TOEIC", color="white", fontsize=14)
    plt.ylabel("Thang điểm TOEIC", color="white", fontsize=14)
    plt.title("Đồ thị điểm TOEIC", color="white", fontsize=18)
    plt.legend(["Điểm TOEIC"], facecolor="#333333", edgecolor="white", labelcolor="white")  # Style legend
    plt.grid(True, color="#555555", linestyle='--')

    # Set Y-axis limits
    plt.ylim(0, 990)
    plt.yticks(np.arange(0, 1000, 100), color="white")  # Y-axis ticks every 100

    # Set X-axis ticks and labels
    plt.xticks(x, x_labels, color="white") # position x_labels to the x axis

    # 3. Convert to Image (Base64)
    buffer = BytesIO()
    plt.savefig(buffer, format='png', facecolor=plt.gcf().get_facecolor())
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png).decode('utf-8')

 # Encode to base64 for embedding in HTML
    if request.user.is_authenticated:
        user_not_login = "hidden"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "hidden"
    context = {
        'user_not_login':user_not_login,
        'user_login':user_login,
        'graphic': graphic
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
    file_name = "vinhdanh.csv"
    file = open(os.path.join(settings.BASE_DIR, f'app\\static\\app\\data\\{file_name}'),encoding='utf-8-sig')
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

# Add this function to test the API key
def test_api_key():
    try:
        genai.configure(api_key=settings.GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content("Hello")
        return True, response.text
    except Exception as e:
        return False, str(e)

@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        # Test API key first
        is_working, test_response = test_api_key()
        if not is_working:
            return JsonResponse({'error': f'API Key error: {test_response}'}, status=500)
            
        try:
            # Debug print to check if API key is loaded
            logger.info(f"API Key present: {bool(settings.GOOGLE_API_KEY)}")
            
            message = request.POST.get('message', '')
            logger.info(f"Received message: {message}")
            
            # Configure Google API
            genai.configure(api_key=settings.GOOGLE_API_KEY)
            
            # Debug print for configuration
            logger.info("Google API configured")
            
            model = genai.GenerativeModel('gemini-2.0-flash')
            logger.info("Model created")
            
            # Create context for the chatbot
            context = """You are Trợ giảng English4All, an AI teaching assistant for an English learning platform. 
            You help students with:
            - English courses (TOEIC, IELTS, THPTQG)
            - Course information and pricing
            - Study materials and resources
            - Online tests and assessments
            - Learning paths and roadmaps
            
            Please respond in Vietnamese unless specifically asked in English.
            Keep responses concise and friendly."""
            
            # Generate response
            prompt = f"{context}\n\nUser: {message}\nTrợ giảng English4All:"
            logger.info("Generating response...")
            response = model.generate_content(prompt)
            logger.info("Response generated")
            
            new_chat = Chatbot_message(message = message, response = response)
            new_chat.save()
            return JsonResponse({'response': response.text})
            
        except Exception as e:
            logger.error(f"Error in chatbot_response: {str(e)}", exc_info=True)
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
