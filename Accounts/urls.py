from django.urls import path
from django.urls import re_path

from .views import get_account_main_page
from .views import create_add
from .views import edit_add
from .views import delete_add

from .views import register
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


app_name='Accounts'
urlpatterns = [
	path('logout/', LogoutView.as_view(), name='Logout'),
	path('login/', LoginView.as_view(template_name='Accounts/login.html'), name='Login'),
	path('register/', register, name='Registration'),

	path('', get_account_main_page, name='AllPostedAdds'),
	path('create/', create_add, name='CreateAdd'),

	path('edit/<int:add_id>/', edit_add, name='EditAdd'),
	path('delete/<int:add_id>/', delete_add, name='DeleteAdd'),
		
]
