from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/',views.RegisterPage, name="register"),
    path('login/',views.LoginPage,name="login"),
    path('logout/',views.logoutPage,name="logout"),
    path('user/',views.user, name='user'),
    path('khoa_hoc/TOEIC/', views.ToiecPage, name="TOEIC"),
    path('khoa_hoc/IELTS/', views.IeltsPage, name="IELTS"),
    path('khoa_hoc/THPTQG/', views.THPTQGPage, name="THPTQG"),
    path('lich_khai_giang/',views.Lich_khai_giangPage, name="lich_khai_giang"),
    path('gioi_thieu/',views.Gioi_thieuPage,name="gioi_thieu"),
    path('user/thong_tin/', views.Thong_tin, name="thong_tin"),
    path('user/thanh_toan/', views.Thanh_toan, name="thanh_toan"),
    path('user/tien_trinh/', views.Tien_trinh, name="tien_trinh"),
    path('test_online/',views.Test_onlinePage, name="test_online"),
    path('vinh_danh/', views.Vinh_danh, name="vinh_danh"),
    path('course/', views.Khoa_hoc, name="course"),
    path('lo_trinh/', views.Lo_trinhPage, name="lo_trinh"),
]
