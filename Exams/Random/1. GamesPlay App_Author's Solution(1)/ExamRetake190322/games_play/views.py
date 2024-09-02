import math
from django.shortcuts import render, redirect
from games_play import models, forms


def home_page(request):
    profile = models.ProfileModel.objects.first()
    context = {'profile': profile}
    return render(request, template_name='home-page.html', context=context)


def create_profile_page(request):
    if request.method == 'POST':
        form = forms.ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = forms.ProfileForm()
    context = {'form': form}
    return render(request, template_name='create-profile.html', context=context)


def dashboard_page(request):
    games = models.GameModel.objects.all()
    all_stars = []
    for game in games:
        ceil_stars = math.ceil(game.rating)
        all_stars.append(ceil_stars)
    context = {'games': games, 'all_stars': all_stars}
    return render(request, template_name='dashboard.html', context=context)


def create_game_page(request):
    if request.method == 'POST':
        form = forms.GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-page')
    else:
        form = forms.GameForm()
    context = {'form': form}
    return render(request, template_name='create-game.html', context=context)


def game_details_page(request, game_id):
    game = models.GameModel.objects.get(id=game_id)
    context = {'game': game}
    return render(request, template_name='details-game.html', context=context)


def edit_game_page(request, game_id):
    game = models.GameModel.objects.get(id=game_id)
    if request.method == "GET":
        context = {'form': forms.GameForm(initial=game.__dict__)}
        return render(request, 'edit-game.html', context)
    else:
        form = forms.GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard-page')
        else:
            context = {'form': form}
            return render(request, 'edit-game.html', context)


def delete_game_page(request, game_id):
    game = models.GameModel.objects.get(id=game_id)
    if request.method == 'POST':
        game.delete()
        return redirect('dashboard-page')

    form = forms.DeleteGameForm(instance=game)
    context = {'form': form}
    return render(request, 'delete-game.html', context)


def profile_details_page(request):
    profile = models.ProfileModel.objects.first()
    all_games = models.GameModel.objects.all()
    total_games = len(all_games)
    try:
        average_rating = sum(game.rating for game in all_games) / total_games
    except ZeroDivisionError:
        average_rating = 0
    context = {'profile': profile, 'total_games': total_games, 'average_rating': average_rating}
    return render(request, template_name='details-profile.html', context=context)


def edit_profile_page(request):
    profile = models.ProfileModel.objects.first()
    if request.method == "GET":
        context = {'form': forms.EditProfileForm(initial=profile.__dict__)}
        return render(request, 'edit-profile.html', context)
    else:
        form = forms.EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-details-page')
        else:
            context = {'form': form}
            return render(request, 'edit-profile.html', context)


def delete_profile_page(request):
    profile = models.ProfileModel.objects.first()
    games = models.GameModel.objects.all()
    if request.method == 'POST':
        profile.delete()
        games.delete()
        return redirect('home-page')

    return render(request, 'delete-profile.html')
