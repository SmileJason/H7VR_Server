#coding: utf-8
from django.contrib import admin
from product.models import (Tag, TagCategory,)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'preview_admin', 'category', 'type', 'parent', 'order', 'created_time', 'last_modified')
    list_filter = ('type', 'category')
    search_fields = ('name',)
    
admin.site.register(Tag, TagAdmin)


class TagCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'order', 'preview_admin')
    list_filter = ('type',)
    search_fields = ('name',)
    
admin.site.register(TagCategory, TagCategoryAdmin)
