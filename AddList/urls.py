from django.urls import re_path
from django.urls import path

from .views import get_user_page
from .views import get_add_page
from .views import get_all_adds


app_name='AddList'
urlpatterns = [
    re_path(r'^adds/(?P<id>.+)$', get_add_page, name='GetAdd'),
    re_path(r'^users/(?P<uuid>.+)$', get_user_page, name='GetUser'),
    path('', get_all_adds, name='GetAllAdds')

]