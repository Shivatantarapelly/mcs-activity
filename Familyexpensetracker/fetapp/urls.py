from django.urls import path

from fetapp import views

urlpatterns = [
    path('home', views.home),
    path('add', views.add),
    path('viewmember', views.viewmember),
    path('addexp', views.addexpense),
    path('addmem', views.addmember),
    path('edit/<int:id>', views.editexpense),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.deleteexpense),
    path('viewfamily', views.viewfamily),
    path('deletemem/<int:id>', views.deletemem),
    path('editmem/<int:id>', views.editmem),
    path('updatemem/<int:id>', views.updatemem),
    path('add_new_mem', views.addnewmem),
    path('redhome', views.redhome),

]
