from django.contrib import admin
from .models import empResume


@admin.register(empResume)
class empResumeAdmin(admin.ModelAdmin):
    list_display = ('fullName', 'positionAppliedFor', 'totalExp', 'currentCTC', 'noticePeriod', 'relocation', 'modifiedDate', 'createdDate')
    list_display_links = ('fullName',)

    fieldsets = [
        ('Employee Resumes', {'fields': ['positionAppliedFor', 'fullName', 'totalExp', 'currentCTC', 'noticePeriod',
                                         'relocation', 'whatsapp', 'email', 'currentRole', 'changeReason',
                                         'currentOrganisation', 'academicQualification', 'technicalCertification',
                                         'uploadCV', 'status']}),
    ]