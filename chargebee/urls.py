from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='chargebee_index'),
    path('/subscribe-now', views.subscribe_now, name='chargebee_subscribe_now'),
    path('/customer-portal', views.customer_portal, name='chargebee_customer_portal'),
]
