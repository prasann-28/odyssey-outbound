from django.db import models
import datetime

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='destinations')
    cities = models.ManyToManyField(City)
    
    def __str__(self):
        return self.name
    
class Tour(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Package(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    destinations = models.ManyToManyField('Destination', related_name='packages')
    image = models.TextField()
    # Add more fields as needed, such as itinerary, departure dates, etc.

    def __str__(self):
        return self.name

class Customer(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone = models.CharField(max_length=10)
	email = models.EmailField(max_length=100)
	password = models.CharField(max_length=100)

class OrderTour(models.Model):
	product = models.ForeignKey(Tour, on_delete=models.CASCADE)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	address = models.CharField(max_length=100, default='', blank=True)
	phone = models.CharField(max_length=20, default='', blank=True)
	date = models.DateField(default=datetime.datetime.today)
	status = models.BooleanField(default=False)
