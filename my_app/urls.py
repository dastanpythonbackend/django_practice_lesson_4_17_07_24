from django.urls import path
from .views import index, registration_view, login_view, dashboard_view, logout_view, profile_view, user_view, set_cookie_view, show_cookie_view, delete_cookie_view

urlpatterns = [
    path('', index, name='index'),
    path('registration/', registration_view, name='registration'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('user/', user_view, name='user'),
    path('set_cookie/', set_cookie_view, name='set_cookie'),
    path('show_cookie/', show_cookie_view, name='show_cookie'),
    path('delete_cookie/', delete_cookie_view, name='delete_cookie'),
]