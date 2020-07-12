from django.urls import path

from .views import PasswordList

urlpatterns = [
    path('', PasswordList.as_view()),
]
