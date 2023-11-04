from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

status_choices = (
    ('Published', 'Published'),
    ('Draft', 'Draft'),
    ('Archived', 'Archived'),
)


class company(models.Model):
    name = models.CharField(_('Company Name'), max_length=255, null=True)
    profile = RichTextField(_('Company Profile'), null=True, blank=True)
    contact = models.CharField(_('Company Contact'), max_length=500, null=True, blank=True)
    website = models.URLField(_('Company Website'), max_length=500, null=True, blank=True)
    address = models.CharField(_('Company Address'), max_length=500, null=True)
    logo = models.ImageField(_('Company Logo'), upload_to='logo/%Y/%m/%d', null=True, blank=True)
    status = models.CharField(_('Status'), choices=status_choices, max_length=10, default='Submitted', null=True)
    createdDate = models.DateTimeField(_('Created Date'), auto_now_add=True, editable=False)
    modifiedDate = models.DateTimeField(_('Modified Date'), auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Company'
        db_table = 'employer-company-list'

    def __str__(self):
        return self.name


class jobs(models.Model):
    company = models.ForeignKey(company, on_delete=models.CASCADE, null=True)
    title = models.CharField(_('Job Title'), max_length=500, null=True)
    experience = models.CharField(_('Experience'), max_length=500, null=True)
    salary = models.CharField(_('Salary'), max_length=500, null=True)
    location = models.CharField(_('Location'), max_length=500, null=True)
    jd = RichTextField(_('Job Description'), null=True)
    role = models.CharField(_('Role'), max_length=500, null=True)
    industry = models.CharField(_('Industry'), max_length=500, null=True)
    department = models.CharField(_('Department'), max_length=500, null=True)
    roleCategory = models.CharField(_('Role Category'), max_length=500, null=True)
    empType = models.CharField(_('Employment Type'), max_length=500, null=True)
    keySkills = models.CharField(_('Key Skills'), max_length=500, null=True)
    education = models.CharField(_('Education'), max_length=500, null=True)
    status = models.CharField(_('Status'), choices=status_choices, max_length=10, default='Submitted', null=True)
    createdDate = models.DateTimeField(_('Created Date'), auto_now_add=True, editable=False)
    modifiedDate = models.DateTimeField(_('Modified Date'), auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
        db_table = 'employer-job-list'

    def __str__(self):
        return self.title