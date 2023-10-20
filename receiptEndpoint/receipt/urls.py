from django.urls import path, re_path
from . import views

urlpatterns = [
    path('receipts/process', views.ReceiptView.as_view()),
    re_path(r'^receipts/(?P<id>\S{36})/points', views.ReceiptView.as_view())
]