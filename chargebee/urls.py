from django.urls import path
from . import views


app_name = 'chargebee'

urlpatterns = [
    path('', views.index, name='index'),
    path('subscribe-now', views.subscribe_now, name='subscribe_now'),
    path('customer-portal', views.customer_portal, name='customer_portal'),
]
