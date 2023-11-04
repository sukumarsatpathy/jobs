from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib import admin
from .models import Account
from django.utils.html import format_html


class AccountAdmin(UserAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%">'.format(object.image.url))
    thumbnail.short_description = 'Image'
    list_display = ('thumbnail','username', 'first_name', 'last_name', 'email', 'is_active', 'last_login', 'date_joined')
    list_display_links = ('username',)
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()

    fieldsets = [
        ('Login Details', {'fields': ['email', 'username', 'password']}),
        ('Basic Details', {'fields': ['first_name', 'last_name', 'contact']}),
        ('Registration Type', {'fields': ['image',]}),
        ('Permission Details', {'fields': ['is_admin', 'is_staff', 'is_active', 'is_superuser']}),
    ]

    add_fieldsets = [
        ('Login Details', {'fields': ['email', 'username', 'password1', 'password2']}),
        ('Basic Details', {'fields': ['first_name', 'last_name', 'contact']}),
        ('Registration Type', {'fields': ['image',]}),
        ('Permission Details', {'fields': ['is_admin', 'is_staff', 'is_active', 'is_superuser']}),
    ]


admin.site.register(Account, AccountAdmin)
admin.site.unregister(Group)
