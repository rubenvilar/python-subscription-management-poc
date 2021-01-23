from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
    template = loader.get_template('chargebee/index.html')
    return HttpResponse(template.render({}, request))


def subscribe_now(request):
    return render(request, 'chargebee/subscribe_now.html')


def customer_portal(request):
    return render(request, 'chargebee/customer_portal.html')
