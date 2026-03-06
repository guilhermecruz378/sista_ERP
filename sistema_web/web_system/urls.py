from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from core import views 


urlpatterns = [
    path('admin/', admin.site.urls),

    #rota de login
    path('accounts/login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),

    #rota de logout
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    #rota de cadastro
    path('', views.home, name='home'),
    path('cadastro/', views.cadastrar_produto, name='cadastro')

]
