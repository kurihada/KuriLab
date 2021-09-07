from django.urls import path
from user.views import *

app_name = 'user'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('personal/', user_personal, name='personal'),
    path('personal_alt/', user_personal_alt, name='personal_alt'),
]
