from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/',views.RegisterPage, name="register"),
    path('login/',views.LoginPage,name="login"),
    path('logout/',views.logoutPage,name="logout"),
    path('user/',views.user, name='user'),
    path('ve_chung_toi/He_thong_co_so/',views.He_thong_co_soPage, name="he_thong_co_so" ),
    path('ve_chung_toi/Tin_tuc/',views.Tin_tucPage, name="tin_tuc"),
    path('ve_chung_toi/Tuyen_dung/',views.Tuyen_dungPage, name="tuyen_dung"),
    path('khoa_hoc/TOEIC/', views.ToiecPage, name="TOEIC"),
    path('khoa_hoc/IELTS/', views.IeltsPage, name="IELTS"),
    path('khoa_hoc/APTIS/', views.AptisPage, name="APTIS"),
    path('lich_khai_giang/',views.Lich_khai_giangPage, name="lich_khai_giang"),
    path('giao_vien/',views.Giao_vienPage,name="giao_vien"),
    path('user/thong_tin/', views.Thong_tin, name="thong_tin"),
    path('user/thanh_toan/', views.Thanh_toan, name="thanh_toan"),
    path('user/tien_trinh/', views.Tien_trinh, name="tien_trinh"),
    path('test_online/',views.Test_onlinePage, name="test_online"),
]
