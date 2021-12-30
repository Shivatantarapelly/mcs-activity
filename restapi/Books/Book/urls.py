from django.urls import path
from .views import *

urlpatterns = [
    path('', book_list),
    path('add/', post_book),
    path('update/<int:id>/', update_book),
    path('delete/<int:id>/', delete_book),

]
