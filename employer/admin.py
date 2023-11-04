from django.contrib import admin
from .models import company, jobs


@admin.register(company)
class companyAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile', 'contact', 'logo', 'status', 'modifiedDate', 'createdDate')
    list_display_links = ('name',)

    fieldsets = [
        ('Employee Resumes', {'fields': ['name', 'profile', 'contact', 'website', 'address', 'logo', 'status']}),
    ]


@admin.register(jobs)
class jobsAdmin(admin.ModelAdmin):
    list_display = ('company', 'title', 'modifiedDate', 'createdDate')
    list_display_links = ('company', 'title',)

    fieldsets = [
        ('Employee Resumes', {'fields': ['company', 'title', 'jd', 'status']}),
    ]