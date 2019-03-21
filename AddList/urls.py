from django.urls import re_path
from django.urls import path

from .views import get_user_page
from .views import get_add_page
from .views import get_all_adds


app_name='AddList'
urlpatterns = [
    path('', get_all_adds, name='GetAllAdds'),
    path('adds/<int:id>/', get_add_page, name='GetAdd'),
    path('users/<int:id>/', get_user_page, name='GetUser'),
]