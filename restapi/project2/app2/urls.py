from django.urls import path
from .views import *

urlpatterns = [
    # path('', StudentList.as_view()),
    # path('add/', StudentCreate.as_view()),
    # path('retrieve/<int:pk>', StudentRetrieve.as_view()),
    # path('update/<int:pk>/', StudentUpdate.as_view()),
    # path('delete/<int:pk>/', StudentDelete.as_view()),
    path('', StudentListCrete.as_view()),
    path('retrieve/<int:pk>', StudentRetDisDel.as_view()),

]
