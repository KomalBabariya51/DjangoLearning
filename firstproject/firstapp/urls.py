
from django.urls import path
from firstapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('formpage/', views.form_view, name='Form'),
    path('logincreate/', views.LoginCreate.as_view(), name='LoginCreate'),
    path('logingetall/', views.GetAllLogin.as_view(), name='LoginGetAll'),
    path('loginlist/', views.ListLogin.as_view(), name='Loginlist'),
    path('teammembers/', views.TeamMembers.as_view(), name='TeamMembers'),
    path('managers/', views.Managers.as_view(), name='Managers'),
    path('employees/', views.Employees.as_view(), name='Employees'),

]