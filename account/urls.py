from django.urls import path
from .views import get_csrf, loginView, WhoAmIView
app_name = 'account'

urlpatterns = [
    path('csrf/', get_csrf, name='api-csrf'),
    path('login/', loginView, name='api-login'),
    path('whoami/', WhoAmIView.as_view(), name='whoami'),
]
