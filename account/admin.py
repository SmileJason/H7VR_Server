#coding: utf-8

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages

from account.models import VRUser

class UserAddAdminForm(UserCreationForm):
    class Meta:
        model = VRUser
        fields = "__all__"

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            self._meta.model._default_manager.get(username=username)
        except self._meta.model.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

 
class UserChangeAdminForm(UserChangeForm):
    class Meta:
        model = VRUser
        fields = "__all__"


class VRUserAdmin(UserAdmin):
    form = UserChangeAdminForm
    add_form = UserAddAdminForm
    list_display = ('username', 'first_name', 'type', 'email', 'is_staff', 'is_active', 'date_joined', 'last_login')
    search_fields = ('username', 'first_name',)
    list_filter = ('type', 'is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('username', 'type', 'security', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'gender', 'birthday', 'email', 'avatar', 
            'mobile', 'phone',  'address')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'type', )}
        ),
    )

    def get_list_display(self, request):
        if request.user.is_superuser:
            return self.list_display
        return ('username', 'first_name', 'type', 'email', 'date_joined', 'last_login')

    def get_queryset(self, request):
        qs = super(VRUserAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(type__in=('1', '8'), is_active=True)
        return qs

    def change_view(self, request, object_id, form_url='', extra_context=None):
        allowed = False
        if request.user.is_superuser:
            allowed = True

        if allowed:
            return super(VRUserAdmin, self).change_view(request, object_id, form_url, extra_context)

        self.message_user(request, u'操作失败，你不能更改用户信息', messages.ERROR)
        return HttpResponseRedirect('/admin')
    
admin.site.register(VRUser, VRUserAdmin)
