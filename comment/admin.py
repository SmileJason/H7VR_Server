#coding: utf-8

from django.contrib import admin
from comment.models import PageComment


class PageCommentAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'user', 'created_time', 'fake_user', 'fake_time')
    list_filter = ('created_time',)
    readonly_fields = ('user', 'created_time')
    search_fields = ('fake_user', 'content',)

    def save_model(self, request, obj, form, change):
        if not change and obj.fake_user:
            obj.user = request.user
        obj.save()

admin.site.register(PageComment, PageCommentAdmin)
