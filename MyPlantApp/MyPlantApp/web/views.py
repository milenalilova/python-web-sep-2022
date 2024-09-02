from django.shortcuts import render, redirect

from MyPlantApp.web.forms import ProfileCreateForm, PlantCreateForm
from MyPlantApp.web.models import Profile, Plant


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'core/home-page.html', context)


def catalogue_page(request):
    plants = Plant.objects.all()
    profile = Profile.objects.first()

    context = {
        'profile': profile,
        'plants': plants,
    }

    return render(request, 'core/catalogue.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }
    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    return render(request, 'profile/profile-details.html', )


def profile_edit(request):
    return render(request, 'profile/edit-profile.html', )


def profile_delete(request):
    return render(request, 'profile/delete-profile.html', )


def plant_create(request):
    if request.method == 'GET':
        form = PlantCreateForm

    else:
        form = PlantCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }
    return render(request, 'plant/create-plant.html', context)


def plant_details(request, pk):
    return render(request, 'plant/plant-details.html', )


def plant_edit(request, pk):
    return render(request, 'plant/edit-plant.html', )


def plant_delete(request, pk):
    return render(request, 'plant/delete-plant.html', )
