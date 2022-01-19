from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import TaskList, CustomLoginView, RegisterPage

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', TaskList.as_view(), name='tasks'),
    path('register/', RegisterPage.as_view(), name='register'),
]