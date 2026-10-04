from .models import car


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.db import models


def home(request):
    return render(request, template_name="myapp/home.html")


def about(request):
    return render(request, template_name="myapp/about.html")


def help(request):
    return render(request, template_name="help.html")


def car_list(request):
    q = request.GET.get("q", "")
    if q:
        cars = car.objects.filter(
            models.Q(car_name__icontains=q) | models.Q(description__icontains=q)
        )
    else:
        cars = car.objects.all()
    context = {"cars": cars}
    return render(request, template_name="myapp/all_cars.html", context=context)


def car_details(request, id):
    car_obj = get_object_or_404(car, id=id)
    return render(request, "myapp/details_car.html", {"car": car_obj})


def upload_car(request):
    form = carForm()
    if request.method == "POST":
        form = carForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("all_cars")
    context = {"form": form}
    return render(request, template_name="myapp/car_form.html", context=context)


def update_car(request, id):
    car_obj = car.objects.get(pk=id)
    form = carForm(instance=car_obj)
    if request.method == "POST":
        form = carForm(request.POST, request.FILES, instance=car_obj)
        if form.is_valid():
            form.save()
            return redirect("all_cars")
    context = {"form": form}
    return render(request, template_name="myapp/car_form.html", context=context)


def delete_car(request, id):
    car_obj = car.objects.get(pk=id)
    if request.method == "POST":
        car_obj.delete()
        return redirect("all_cars")
    return render(request, template_name="myapp/delete_car.html")


def purchase_car(request, car_id):
    car_obj = get_object_or_404(car, id=car_id)
    if request.method == "POST":
        if request.user.is_authenticated:
            from .models import Purchase

            with_driver = request.POST.get("with_driver") == "on"
            from_date = request.POST.get("from_date")
            to_date = request.POST.get("to_date")
            Purchase.objects.create(
                user=request.user,
                car=car_obj,
                with_driver=with_driver,
                from_date=from_date,
                to_date=to_date,
            )
            return redirect("profile")
    return render(request, "purchase-car.html", {"car": car_obj})


def contact(request):
    return render(request, "contact.html")
