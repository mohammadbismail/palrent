
from django.shortcuts import render, redirect
from user_app.models import Provider
from .models import Car


def my_dashboard(request):

    if "customer_id" not in request.session:
        return redirect("/")

    return render(request,"my_dashboard.html")

def search(request):

    request.session["location"] = request.POST['location']
    request.session["pick_up_date"] = request.POST['pick_up_date']
    request.session["drop_off_date"] = request.POST['drop_off_date']

    return redirect("/search_result")


def search_result(request):


    context = {
        'searched_cars': Provider.objects.filter(location=request.session["location"])
    }

    return render(request,"search_result.html", context)

def car_select(request, car_id):
    return redirect("/car_details/"+car_id)

def car_details(request, car_id):
    context = {
        'selected_car': Car.objects.get(id=car_id)
    }
    return render(request,"car_details.html", context)

def car_book(request):
    return redirect("/register")

def payment_method(request):
    return render(request,"payment_method.html")

def payment_confirmation(request):
    return render(request,"payment_confirmation.html")

def confirm_book(request):
    return redirect("/")

def provider_dashboard(request):
    return render(request,"provider_dashboard.html")


def add_car(request):
    print("this works here")

    context = {
        'cars': Car.objects.filter(provider=request.session["provider_id"])
    }
    return render(request,"add_car.html", context)

def insert_car(request):

    Car.objects.create(
            brand = request.POST['brand'],
            model = request.POST['model'],
            color = request.POST['color'],
            production_year = request.POST['production_year'],
            plate_number = request.POST['plate_number'],
            price = request.POST['price'],
            provider = Provider.objects.get(id=request.session['provider_id'])
        )
    return redirect("/my_dashboard/add_car")

def edit_car(request, car_id):

    context = {
        'garage': Car.objects.filter(provider=request.session["provider_id"]),
        'car_id': car_id,
        'car': Car.objects.get(id=car_id)
    }
    return render(request,"edit_car.html", context)

def edit_my_car(request, car_id):

    print("this works here")

    # car_id = request.POST['car_id']
    c = Car.objects.get(id=car_id)
    c.brand = request.POST['brand']
    c.model = request.POST['model']
    c.color = request.POST['color']
    c.production_year = request.POST['production_year']
    c.plate_number = request.POST['plate_number']
    c.price = request.POST['price']
    c.save()

    return redirect("/my_dashboard/edit_car/"+car_id)



