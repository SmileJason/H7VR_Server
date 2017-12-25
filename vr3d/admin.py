# coding=utf-8
from django.contrib import admin

from vr3d.models import VR3D

class VR3DAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'creator', 'status', 'created_time')
    list_filter = ('status', 'tag', 'creator')
    search_fields = ('title',)
    filter_horizontal = ('tag',)

    def get_queryset(self, request):
        qs = super(VR3DAdmin, self).get_queryset(request)
        return qs

admin.site.register(VR3D, VR3DAdmin)