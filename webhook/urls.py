from django.urls import path
from .views import opt_out, daily, weekly

urlpatterns = [
    path('email-settings/daily/', daily, name='daily'),
    path('email-settings/weekly/', weekly, name='weekly'),
    path('email-settings/opt-out/', opt_out, name='opt_out'),
]
