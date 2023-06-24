from django.urls import path 
from otp_app.views import (RegisterView, LoginView, GenerateOTP)

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('otp/generate', GenerateOTP.as_view()),
]