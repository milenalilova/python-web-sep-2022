from django.contrib import admin

from my_music_app2.web.models import Profile, Album


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Album)
class ALbumAdmin(admin.ModelAdmin):
    pass
