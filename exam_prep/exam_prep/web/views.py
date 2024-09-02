from django.shortcuts import render, redirect

from exam_prep.web.forms import ProfileCreateForm
from exam_prep.web.models import Profile, Album


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        return redirect('add profile')

    context = {
        'albums': Album.objects.all()
    }
    return render(request, 'core/home-with-profile.html', context,)


def add_album(request):
    return render(request, 'albums/add-album.html')


def details_album(request, pk):
    return render(request, 'albums/album-details.html')


def edit_album(request, pk):
    return render(request, 'albums/edit-album.html')


def delete_album(request, pk):
    return render(request, 'albums/delete-album.html')


def details_profile(request):
    return render(request, 'profiles/profile-details.html')


def add_profile(request):
    if get_profile() is not None:
        return redirect('index')

    if request.method == 'GET':
        form = ProfileCreateForm
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'core/home-no-profile.html', context)


def delete_profile(request):
    return render(request, 'profiles/profile-delete.html')
