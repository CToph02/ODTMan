from django.urls import path
from .views import user_register, user_login, user_logout, user_pwd_change

urlpatterns = [
    path('register/', user_register.as_view(), name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('change-password/', user_pwd_change, name='change_password')

]