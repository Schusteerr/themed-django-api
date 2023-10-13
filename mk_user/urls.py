from django.urls import path
from app_mk_user import views

urlpatterns = [
    path('',views.home,name='index'),
    path('users/',views.users,name='listen_users')
]
