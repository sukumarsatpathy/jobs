from django.db import models
from django.utils.translation import gettext_lazy as _


status_choices = (
    ('Submitted', 'Submitted'),
    ('Rejected', 'Rejected'),
)

relocation_choice = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)


class empResume(models.Model):
    positionAppliedFor = models.CharField(_('Position Applied For'), max_length=500, null=True)
    fullName = models.CharField(_('Full Name'), max_length=200, null=True)
    totalExp = models.CharField(_('Total Experience'), max_length=200, null=True)
    currentCTC = models.CharField(_('Current CTC'), max_length=200, null=True)
    noticePeriod = models.CharField(_('Notice Period'), max_length=200, null=True)
    relocation = models.CharField(_('Relocation'), choices=relocation_choice, max_length=10, null=True)
    mobile = models.CharField(_('Mobile'), max_length=20, null=True)
    whatsapp = models.CharField(_('Mobile'), max_length=20, null=True)
    email = models.CharField(_('Email'), max_length=500, null=True)
    currentRole = models.CharField(_('Current Role'), max_length=500, null=True)
    changeReason = models.CharField(_('Change Reason'), max_length=500, null=True)
    currentOrganisation = models.CharField(_('Current Organisation'), max_length=500, null=True)
    academicQualification = models.CharField(_('Academic Qualification'), max_length=500, null=True)
    technicalCertification = models.CharField(_('Technical Certification'), max_length=500, null=True)
    uploadCV = models.FileField(_('Upload CV'), upload_to='cv/%Y/%m/%d', null=True)
    status = models.CharField(_('Status'), choices=status_choices, max_length=10, default='Submitted', null=True)
    createdDate = models.DateTimeField(_('Created Date'), auto_now_add=True, editable=False)
    modifiedDate = models.DateTimeField(_('Modified Date'), auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Employee CV'
        verbose_name_plural = 'Employee CV'
        db_table = 'emp-cv-list'

    def __str__(self):
        return self.fullName