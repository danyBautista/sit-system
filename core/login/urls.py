from django.urls import path
from core.login.views import LoginFormView, LogoutView, LogoutRedirecView

urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),
    path('logout', LogoutRedirecView.as_view(), name='logout')
]