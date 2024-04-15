from django.shortcuts import render, redirect
from .models import Destination, Package
from json import dumps 

# Create your views here.
def home(request):
	# products = Product.objects.all()
	return render(request, 'home.html', {})

def destinations(request):
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
    'terms': terms
}
		destinations = Destination.objects.all()
		return render(request, 'destinations.html', {'destinations' : destinations, 'user' : user})
	else:
		return redirect('home')

def packages(request):
	
	if request.method == "POST":
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		email = request.POST['email']
		phone = request.POST['phone']
		querycategory = request.POST['querycategory']
		queryaddn = request.POST['queryaddn']
		terms = request.POST['terms']
		selected_country = request.POST['flexRadioDefault']
		user = {
    'firstname': firstname,
    'lastname': lastname,
    'email': email,
    'phone': phone,
    'querycategory': querycategory,
    'queryaddn': queryaddn,
    'terms': terms}
		packages = Package.objects.filter(destinations__name=selected_country)

		cost_estimates = {}
		for package in packages:
			cost_estimates[package.name] = estimate_cost(package_name=package.name, destination=selected_country)
		if len(packages) == 0:
			return redirect('home')
		cost_estimates = dumps(cost_estimates)
		return render(request, 'packages.html', {'packages' : packages, 'selected_country': selected_country, 'cost_estimates': cost_estimates})
	else:
		return redirect('home')

package_prices = {"Family Fun Package": 1500, "Relaxation Retreat Package": 2500 , "Cultural Immersion Package": 1800, "Adventure Seeker Package": 2000 }
destination_prices = {"Japan": 150, "Ireland": 100, "United States": 175, "United Kingdom": 100}
def estimate_cost(package_name, destination):
    package_price = int(package_prices[package_name])
    total_package_cost = int(package_price)

    # Add the total package cost to the total destination cost to get the overall estimate
    total_cost = total_package_cost + int(destination_prices[destination])

    return total_cost
