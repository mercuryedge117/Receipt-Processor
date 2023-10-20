from django.urls import path, re_path
from . import views

urlpatterns = [
    path('process', views.ReceiptView.as_view()),
    re_path(r'^(?P<id>\S+)/points', views.ReceiptView.as_view())
]