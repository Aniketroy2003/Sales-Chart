from django.shortcuts import render
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.core.cache import cache
from .models import SalesData
import json
from django.core.serializers.json import DjangoJSONEncoder

def get_monthly_sales():
    cached_data = cache.get('monthly_sales')
    if cached_data:
        return json.loads(cached_data)

    sales = (SalesData.objects
             .annotate(month=TruncMonth('sale_date'))
             .values('month')
             .annotate(total_amount=Sum('amount'))
             .order_by('month'))
    
    # Converting dates for serialized json data
    sales_data = [
        {
            'month': item['month'].strftime('%Y-%m-%d'),
            'total_amount': item['total_amount']
        }
        for item in sales
    ]

    
    cache.set('monthly_sales', json.dumps(sales_data, cls=DjangoJSONEncoder), timeout=3600)

    return sales_data

def sales_chart(request):
    data = get_monthly_sales()
    return render(request, 'sales_chart.html', {'data': data})
