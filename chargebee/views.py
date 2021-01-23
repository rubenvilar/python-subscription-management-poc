from django.http import HttpResponse


def index(request):
    return HttpResponse("Here you can show the two options bellow.")


def subscribe_now(request):
    return HttpResponse("Subscribe Now")


def customer_portal(request):
    return HttpResponse("Customer Portal")
