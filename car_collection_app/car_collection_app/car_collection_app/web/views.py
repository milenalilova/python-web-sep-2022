from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html', )


def catalogue(request):
    return render(request, 'core/catalogue.html', )


def create_car(request):
    return render(request, 'cars/car-create.html', )


def details_car(request, pk):
    return render(request, 'cars/car-details.html', )


def edit_car(request, pk):
    return render(request, 'cars/car-edit.html', )


def delete_car(request, pk):
    return render(request, 'cars/car-delete.html', )


def create_profile(request):
    return render(request, 'profiles/profile-create.html', )


def details_profile(request):
    return render(request, 'profiles/profile-details.html', )


def edit_profile(request):
    return render(request, 'profiles/profile-edit.html', )


def delete_profile(request):
    return render(request, 'profiles/profile-delete.html', )
