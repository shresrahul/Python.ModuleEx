
from django.contrib.auth.views import LoginView
from .views import signup, TransactionView

urlpatterns = [
    path('signup/', signup, name='signup'),
    # # class based views ma as_view() method call garnu parxa 
    path('send/', TransactionView.as_view(), name="send"),
    path('login/', LoginView.as_view(template_name = 'login.html'), name='login'), 
]