# from django.urls import path
# from .views import UserRegistrationView

# urlpatterns = [
#     path('api/register/', UserRegistrationView.as_view(), name='user-register'),
# ]
from django.urls import path
from .views import UserRegistrationView
from .views import UserLoginView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
     path('login/', UserLoginView.as_view(), name='user-login'),
]