from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import RegexValidator


status_choices = (
    ('Published', 'Published'),
    ('Under Review','Under Review'),
    ('Draft', 'Draft'),
    ('Declined', 'Declined'),
)

key_type_choices = (
    ('Live', 'Live'),
    ('Test', 'Test'),
)

email_choices = (
    ('True', 'True'),
    ('False', 'False'),
)

phone_validator = RegexValidator(r"^(\+?\d{0,4})?\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{4}\)?)?$",
                                 "The phone number provided is invalid")


class WebSettings(models.Model):
    # Brand
    title = models.CharField(_('Brand Name'), max_length=255, null=True)
    slogan = models.CharField(_('Slogan'), max_length=255, null=True)
    # Logo
    logo_dark = models.ImageField(_('Logo Dark'), upload_to='settings/logo/%Y/%m/%d/')
    logo_light = models.ImageField(_('Logo Light'), upload_to='settings/logo/%Y/%m/%d/')
    favicon = models.FileField(_('Favicon'), upload_to='settings/favicon/%Y/%m/%d/')
    # Contact
    contact_email = models.EmailField(_('Contact Email'), max_length=255, null=True)
    contact_number = models.CharField(_('Contact Number'), max_length=20, validators=[phone_validator], null=True)
    contact_address = models.CharField(_('Contact Address'), max_length=500, null=True)
    # Invoice
    company_name = models.CharField(_('Registered Company Name'), max_length=500, null=True, blank=True)
    company_address = models.CharField(_('Registered Company Address'), max_length=500, null=True, blank=True)
    company_gst = models.CharField(_('Goods and Service Tax'), max_length=50, null=True, blank=True)
    # Default User
    default_user = models.ImageField(_('Default User Image'), upload_to='settings/user/%Y/%m/%d/', null=True)
    # Google reCaptcha V3
    public_key = models.CharField(_('Google reCaptcha Public Key'), max_length=255, null=True, blank=True)
    private_key = models.CharField(_('Google reCaptcha Private Key'), max_length=255, null=True, blank=True)
    # SEO
    meta_title = models.CharField(_('Meta Title'), max_length=60, null=True)
    meta_description = models.CharField(_('Meta Description'), max_length=158, null=True)
    meta_keywords = models.CharField(_('Meta Keywords'), max_length=255, null=True)

    created = models.DateTimeField(_('Created Date'), auto_now_add=True, editable=False)
    modified = models.DateTimeField(_('Modified Date'), auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Web Setting'
        verbose_name_plural = 'Web Settings'
        db_table = 'settings-website'

    def __str__(self):
        return self.title


class MailServer(models.Model):
    name = models.CharField(_('SMTP From Name'), max_length=100, null=True)
    email = models.EmailField(_('SMTP From Email'), max_length=100, null=True)
    port = models.CharField(_('SMTP Port Number'), max_length=10, null=True)
    host = models.CharField(_('SMTP HOST'), max_length=50, null=True)
    host_user = models.EmailField(_('SMTP Host User'), max_length=100, null=True)
    host_password = models.CharField(_('SMTP Host Password'), max_length=100, null=True)
    use_tls = models.CharField(_('SMTP Use TLS'), max_length=5, choices=email_choices, null=True)
    use_ssl = models.CharField(_('SMTP Use SSL'), max_length=5, choices=email_choices, null=True)
    status = models.CharField(_('Status'), max_length=50, choices=status_choices, default='Published', null=True)
    created = models.DateTimeField(_('Created Date'), auto_now_add=True, editable=False)
    modified = models.DateTimeField(_('Modified Date'), auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Mail Server'
        verbose_name_plural = 'Mail Server'
        db_table = 'settings-mail-server'

    def __str__(self):
        return self.name


class Stripe(models.Model):
    stripe_key_type = models.CharField(_('Stripe Key Type'), max_length=10, choices=key_type_choices, null=True, blank=True)
    stripe_public_key = models.CharField(_('Stripe Public Key'), max_length=255, null=True, blank=True)
    stripe_secret_key = models.CharField(_('Stripe Secret Key'), max_length=255, null=True, blank=True)
    status = models.CharField(_('Status'), max_length=50, choices=status_choices, default='Published', null=True)
    created = models.DateTimeField(_('Created Date'), auto_now_add=True, editable=False, null=True)
    modified = models.DateTimeField(_('Modified Date'), auto_now=True, editable=False, null=True)

    class Meta:
        verbose_name = 'Stripe Payment Gateway'
        verbose_name_plural = 'Stripe Payment Gateway'
        db_table = 'settings-stripe-payment-gateway'

    def __str__(self):
        return str(self.id)


class Twilio(models.Model):
    accountSID = models.CharField(_('Account SID'), max_length=100, null=True)
    authToken = models.CharField(_('Auth Token'), max_length=100, null=True)
    phoneNumber = models.CharField(_('Twilio Number'), max_length=20, null=True)
    status = models.CharField(_('Status'), max_length=50, choices=status_choices, default='Published', null=True)
    created = models.DateTimeField(_('Created Date'), auto_now_add=True, editable=False)
    modified = models.DateTimeField(_('Modified Date'), auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Twilio'
        verbose_name_plural = 'Twilio'
        db_table = 'settings-twilio'

    def __str__(self):
        return self.phoneNumber