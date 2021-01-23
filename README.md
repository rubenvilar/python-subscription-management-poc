# Subscription Management with Python

## Getting Started with Chargebee
- Install Python and Django https://docs.djangoproject.com/en/3.1/intro/tutorial01/
- Sign Up in Chargebee https://www.chargebee.com

#### Creating the project and the Chargebee app
```
django-admin startproject python_subscription_management
python manage.py startapp chargebee
```

### Integrating via Drop-in Script
https://www.chargebee.com/checkout-portal-docs/drop-in-integration.html
- See 'chargebee/templates/chargebee' files
- Easy to install (only frontend changes needed)
- Using pop-ups to create and manage existing subscriptions
- There is no communication with the backend. You will have to manage the subscriptions manually once they are activated or deactivated.
- No option to combine this integration with a webhook or a "return url" to match the Chargebee subscription with you backend entities.

### API Based Integration (pending)

https://www.chargebee.com/checkout-portal-docs/api-checkout.html
https://www.chargebee.com/checkout-portal-docs/api-portal.html

- You use an endpoint in your app to create the subscription, get authenticated urls and redirect the user to it
- The customers will be redirected to a URL upon successful checkout.
- You will have to use webhooks to manage the changes

## Useful Django commands
```
python manage.py runserver
python manage.py migrate
python manage.py createsuperuser
```
