from django.urls import path
from .views import sales_chart

urlpatterns = [
    path('', sales_chart, name='sales_chart'),
]