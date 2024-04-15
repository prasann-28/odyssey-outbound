# Register your models here.
from django.contrib import admin
from .models import Destination, Customer, Tour, OrderTour, Package, City
from django.contrib.auth.models import User

admin.site.register(Destination)
admin.site.register(Customer)
admin.site.register(Tour)
admin.site.register(OrderTour)
admin.site.register(Package)
admin.site.register(City)