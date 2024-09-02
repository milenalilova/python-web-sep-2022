from django.core import exceptions
from django.shortcuts import render, redirect

from car_collection_app.web.forms import CreateProfileForm, CreateCarForm, EditCarForm, DeleteCarForm, EditProfileForm
from car_collection_app.web.models import Profile, Car


def get_profile():
    try:
        return Profile.objects.first()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }

    return render(request, 'core/index.html', context, )


def catalogue(request):
    cars = Car.objects.all()
    profile = Profile.objects.first()
    context = {
        'profile': profile,
        'cars': cars,
    }
    return render(request, 'core/catalogue.html', context)


def create_car(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = CreateCarForm()
    else:
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'cars/car-create.html', context, )


def details_car(request, pk):
    car = Car.objects.filter(pk=pk).get()

    context = {
        'car': car,
    }
    return render(request, 'cars/car-details.html', context, )


def edit_car(request, pk):
    car = Car.objects.get(pk=pk)

    if request.method == 'GET':
        form = EditCarForm(instance=car)
    else:
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'cars/car-edit.html', context, )


def delete_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = DeleteCarForm(instance=car)
    else:
        form = DeleteCarForm(request.POST, instance=car)
        car.delete()
        return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
    }

    return render(request, 'cars/car-delete.html', context, )


def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'profiles/profile-create.html', context)


def details_profile(request):
    profile = Profile.objects.first()
    all_cars = Car.objects.all()
    cars_sum = sum(car.price for car in all_cars)

    context = {
        'profile': profile,
        'cars_sum': cars_sum,
    }

    return render(request, 'profiles/profile-details.html', context, )


def edit_profile(request):
    profile = Profile.objects.first()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'profiles/profile-edit.html', context, )


def delete_profile(request):
    profile = Profile.objects.first()
    cars = Car.objects.all()

    if request.method == 'POST':
        profile.delete()
        cars.delete()
        return redirect('index')

    context = {
        'profile': profile,
    }

    return render(request, 'profiles/profile-delete.html', context, )
