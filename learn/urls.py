from django.contrib import admin
from django.urls import path

from api.views import Signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Signup.as_view()),
]
