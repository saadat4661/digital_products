from django.urls import path

from . import views

urlpatterns = [
    path('packages/', views.PackageView.as_view(), name="package"),
    path('subscriptions/', views.SubscriptionView.as_view(), name="subscription")
]