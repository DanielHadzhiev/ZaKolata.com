from django.urls import path, include
from .views import ClientRegistrationView

urlpatterns = [
    path("register", ClientRegistrationView.as_view(), name='client-register')
]
