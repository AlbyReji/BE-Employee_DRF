from django.urls import path
from .import views

urlpatterns = [
    path('', views.EmployeeCreateList.as_view(), name='employeelist'),
    path('<int:pk>/', views.EmployeeDetail.as_view(), name='employeeDetail'),
]