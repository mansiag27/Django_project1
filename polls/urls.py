# App-level urls.py (polls/urls.py)
from django.urls import path
from . import views

urlpatterns = [
    path('school/', views.create_school, name='create_school'),
    path('student/', views.create_student, name='create_student'),
    path('school/<str:school_id>/', views.delete_school, name='delete_school'),
    path('students/<str:student_id>', views.delete_student, name='delete_student'),
    path('student/<str:student_id>', views.update_student, name='update_student'),
    # path('user/',views.create_user,name='create_user'),
    path('schools/<str:school_id>/students/', views.get_students_by_school, name='get_students_by_school'),
    path('schools/', views.get_schools_with_students, name='get_schools_with_students'), 
    path('create_user/',views.create_user,name='create_user'),
    path('login/', views.login_view, name='login_view')
]
