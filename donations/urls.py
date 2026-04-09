from django.urls import path
from . import views


app_name = 'donations'

urlpatterns = [
    path('donate/', views.donate, name='donate'),
    path('confirm/<uuid:uuid>/', views.confirm, name='donation_confirm'),
    path('success/<uuid:uuid>/', views.success, name='donation_success'),
    path('failure/<uuid:uuid>/', views.failure, name='donation_failure'),
]
