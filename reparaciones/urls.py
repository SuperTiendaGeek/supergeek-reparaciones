from django.urls import path
from .views import login_view, ordenes_view
from django.contrib.auth.views import LogoutView
from .views import ordenes_cliente
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('/login/')

urlpatterns = [
    path('login/', login_view, name='login'),
    path('ordenes/', ordenes_view, name='ordenes'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('mis-ordenes/', ordenes_cliente, name='mis_ordenes'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('logout/', logout_view, name='logout'),
]

