from django.contrib import admin
from playlist.models import PlayList, PlayListGroup


class PlayListGroupInline(admin.TabularInline):
    model = PlayListGroup
    extra = 5


class PlayListAdmin(admin.ModelAdmin):
    inlines = (PlayListGroupInline,)


admin.site.register(PlayList, PlayListAdmin)


