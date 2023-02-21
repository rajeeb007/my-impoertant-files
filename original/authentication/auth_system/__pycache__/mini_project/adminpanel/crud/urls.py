
from django.urls import path
from crud import views

urlpatterns = [
    path('addandshow/', views.add_show, name="addandshow"),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('<int:id>/', views.update_data, name="updatedata"),
    path('search', views.search_username, name="searchusername"),
    path('adminadd', views.adminadd, name="adminadd")
]
