from django.urls import path

from login.views.login import CreateUser, Login

urlpatterns = [
    path('create/user/', CreateUser.as_view(), name="create_user"),
    path('login_user/', Login.as_view(), name="login_user"),
]
