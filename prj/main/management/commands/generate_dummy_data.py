from django.core.management.base import BaseCommand
from main.models import SalesData
from datetime import date, timedelta
import random

class Command(BaseCommand):
    help = 'Generate dummy sales data'

    def handle(self, *args, **kwargs):
        # Define the start date and end date for the dummy data
        start_date = date(2022, 1, 1)
        end_date = date(2023, 12, 31)
        delta = end_date - start_date

        # Clear existing data
        SalesData.objects.all().delete()

        # Generate a sales record for each day in the date range
        for i in range(delta.days + 1):
            current_date = start_date + timedelta(days=i)
            # Generate a random sales amount
            amount = round(random.uniform(100.0, 1000.0), 2)
            SalesData.objects.create(sale_date=current_date, amount=amount)
            self.stdout.write(self.style.SUCCESS(f'Successfully created sales data for {current_date}'))

        self.stdout.write(self.style.SUCCESS('Successfully generated dummy sales data'))
