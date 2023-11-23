from django.urls import path
from . import views

app_name= 'authentication'

urlpatterns=[
    path('home/',views.allCourse,name="allCourse"),
    path('',views.login_page,name="login_page"),
    path('register/',views.register,name="register"),
    path('logout/',views.logout,name="logout"),
    path('studentform/',views.studentform,name="studentform"),
    path('dataform/',views.dataform,name="dataform"),
    path('department/<slug>/',views.department,name="department"),
    path('get-course/', views.get_course_by_id, name="get_course_by_id"),
    ]

