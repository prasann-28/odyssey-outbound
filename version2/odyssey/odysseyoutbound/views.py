from django.shortcuts import render, redirect
from .models import Destination, Package
from json import dumps 

# Create your views here.
def home(request):
	# products = Product.objects.all()
	return render(request, 'home.html', {})

def destinations(request):
	if request.method == "POST":
		numberTravellers = request.POST['customRange1']
		package_selected = request.POST['flexRadioDefault']
		print(numberTravellers, package_selected)
		
		destinations = Destination.objects.all()
		selected_package = Package.objects.get(name=package_selected)
		print(selected_package.destinations.all())
		destinations = selected_package.destinations.all()
		cost_estimates = {}
		for destination in destinations:
			cost_estimates[destination.name] = estimate_cost(num_travelers=numberTravellers, package_name=package_selected, destination=destination.name)
		print(numberTravellers)
		print(str(cost_estimates))

		return render(request, 'destinations.html', {'destinations' : destinations, 'cost_estimates': dumps(cost_estimates)})

def packages(request):
	if request.method == "POST":
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		email = request.POST['email']
		phone = request.POST['phone']
		querycategory = request.POST['querycategory']
		queryaddn = request.POST['queryaddn']
		terms = request.POST['terms']
		user = {
    'firstname': firstname,
    'lastname': lastname,
    'email': email,
    'phone': phone,
    'querycategory': querycategory,
    'queryaddn': queryaddn,
    'terms': terms}
		packages = Package.objects.all()
		print(user)
		return render(request, 'packages.html', {'packages' : packages, 'user': user})
	

package_prices = {"Family Fun Package": 1500, "Relaxation Retreat Package": 2500 , "Cultural Immersion Package": 1800, "Adventure Seeker Package": 2000 }
destination_prices = {"Japan": 150, "Ireland": 100, "United States": 175, "United Kingdom": 100}
def estimate_cost(num_travelers, package_name, destination):
    package_price = int(package_prices[package_name])


    # Add the total package cost to the total destination cost to get the overall estimate
    total_cost = (package_price + int(destination_prices[destination])) * int(num_travelers)

    return total_cost
