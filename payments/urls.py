from django.urls import path

from . import views

urlpatterns = [
    path('gateway/', views.GatewayView.as_view(), name="gateway"),
    path('pay/', views.PaymentView.as_view(), name="payment")
]