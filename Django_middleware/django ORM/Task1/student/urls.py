from django.urls import path
from student import views

app_name = 'student'

urlpatterns = [
    path('', views.student_list_, name='student_data'),
]
