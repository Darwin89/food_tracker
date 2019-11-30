from django.conf.urls import url
from .views import index, add_meal, delete_meal, update_meal, login
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
	url(r'^$', login, name='login'),
	url(r'^$', indexword$, name='index'),
	url(r'^add_meal$', add_meal, name='add-meal'), 
	url(r'^delete_meal/(?P<meal_id>\d+)$', delete_meal, name='delete-meal'),
	url(r'^update_meal/(?P<meal_id>\d+)$', update_meal, name='update-meal'),
	url(r'^admin/', admin.site.urls),
	url(r'^', include(('food.urls',food), namespace="food")),
	url(r'^accounts/login/$', auth_views.LoginView.as_view(template_name= 'login.html’), name='auth_login'), url(r'^accounts/logout/$', auth_views.LogoutView.as_view(next_page='food:login’), name='auth_logout'),
	url(r'^accounts/password/change$', auth_views.PasswordChangeView.as_view (template_name='password_change.html’,success_url=reverse_lazy(’food:login’)),name='auth_password_change')]