from django import forms
from .models import WebSettings, MailServer, Twilio


class WebSettingsForm(forms.ModelForm):
    class Meta:
        model = WebSettings
        fields = ('title', 'slogan', 'logo_dark', 'logo_light', 'favicon', 'contact_email', 'contact_number',
                  'contact_address', 'company_name', 'company_address', 'company_gst', 'meta_title', 'meta_description',
                  'meta_keywords', 'default_user', 'public_key', 'private_key')

    def __init__(self, *args, **kwargs):
        super(WebSettingsForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['slogan'].widget.attrs['class'] = 'form-control'
        self.fields['logo_dark'].widget.attrs['class'] = 'form-control'
        self.fields['logo_light'].widget.attrs['class'] = 'form-control'
        self.fields['favicon'].widget.attrs['class'] = 'form-control'
        self.fields['contact_email'].widget.attrs['class'] = 'form-control'
        self.fields['contact_number'].widget.attrs['class'] = 'form-control'
        self.fields['contact_address'].widget.attrs['class'] = 'form-control'
        self.fields['company_name'].widget.attrs['class'] = 'form-control'
        self.fields['company_address'].widget.attrs['class'] = 'form-control'
        self.fields['company_gst'].widget.attrs['class'] = 'form-control'
        self.fields['meta_title'].widget.attrs['class'] = 'form-control kt_docs_maxlength_basic'
        self.fields['meta_title'].widget.attrs['maxlength'] = '60'
        self.fields['meta_description'].widget.attrs['class'] = 'form-control kt_docs_maxlength_basic'
        self.fields['meta_description'].widget.attrs['maxlength'] = '255'
        self.fields['meta_keywords'].widget.attrs['class'] = 'form-control'
        self.fields['default_user'].widget.attrs['class'] = 'form-control'
        self.fields['public_key'].widget.attrs['class'] = 'form-control'
        self.fields['private_key'].widget.attrs['class'] = 'form-control'
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = 'Provide Detail'


class MailServerForm(forms.ModelForm):
    class Meta:
        model = MailServer
        fields = ('name', 'email', 'port', 'host', 'host_user', 'host_password', 'use_tls', 'use_ssl')

    def __init__(self, *args, **kwargs):
        super(MailServerForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['port'].widget.attrs['class'] = 'form-control'
        self.fields['host'].widget.attrs['class'] = 'form-control'
        self.fields['host_user'].widget.attrs['class'] = 'form-control'
        self.fields['host_password'].widget.attrs['class'] = 'form-control'
        self.fields['use_tls'].widget.attrs['class'] = 'form-select'
        self.fields['use_ssl'].widget.attrs['class'] = 'form-select'
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = 'Provide Detail'


class TwilioForm(forms.ModelForm):
    class Meta:
        model = Twilio
        fields = ('accountSID', 'authToken', 'phoneNumber', 'status')

    def __init__(self, *args, **kwargs):
        super(TwilioForm, self).__init__(*args, **kwargs)
        self.fields['accountSID'].widget.attrs['class'] = 'form-control'
        self.fields['authToken'].widget.attrs['class'] = 'form-control'
        self.fields['phoneNumber'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-select'
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = 'Provide Detail'