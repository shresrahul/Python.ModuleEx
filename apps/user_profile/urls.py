
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import SignUp, TransactionView, UserDetailView

urlpatterns = [
    # path('signup/', signup, name='signup'),
    path('signup/', SignUp.as_view(), name="signup"),
    # # class based views ma as_view() method call garnu parxa 
    path('send/', TransactionView.as_view(), name="send"),
    path('login/', LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('detail/', UserDetailView.as_view(), name='user-detail'),
]
