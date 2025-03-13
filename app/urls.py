from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/',views.RegisterPage, name="register"),
    path('login/',views.LoginPage,name="login"),
    path('logout/',views.logoutPage,name="logout"),
    path('khoa_hoc/TOEIC/', views.ToiecPage, name="TOEIC"),
    path('khoa_hoc/IELTS/', views.IeltsPage, name="IELTS"),
    path('khoa_hoc/THPTQG/', views.THPTQGPage, name="THPTQG"),
    path('tai_lieu/',views.Tai_lieuPage, name="tai_lieu"),
    path('gioi_thieu/',views.Gioi_thieuPage,name="gioi_thieu"),
    path('user/thong_tin/', views.Thong_tin, name="thong_tin"),
    path('user/thanh_toan/', views.Thanh_toan, name="thanh_toan"),
    path('test_online/',views.Test_onlinePage, name="test_online"),
    path('vinh_danh/', views.Vinh_danh, name="vinh_danh"),
    path('course/', views.Khoa_hoc, name="course"),
    path('lo_trinh/', views.Lo_trinhPage, name="lo_trinh"),
    path('user/cap_nhat_thong_tin/', views.Cap_nhat_thong_tinPage, name="cap_nhat_thong_tin"),
    path('user/thay_doi_mat_khau/', views.Thay_doi_mat_khauPage, name="thay_doi_mat_khau"),
    path('flash_card/',views.Flash_CardPage, name="flash_card")
]
