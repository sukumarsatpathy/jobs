from django import forms
from django.core import validators
from .models import empResume
from django.forms import CharField


class empResumeForm(forms.ModelForm):
    class Meta:
        model = empResume
        fields = ('positionAppliedFor', 'fullName', 'totalExp', 'currentCTC', 'noticePeriod', 'relocation', 'whatsapp',
                  'email', 'currentRole', 'changeReason', 'currentOrganisation', 'academicQualification',
                  'technicalCertification', 'uploadCV')

    def __init__(self, *args, **kwargs):
        super(empResumeForm, self).__init__(*args, **kwargs)
        self.fields['positionAppliedFor'].widget.attrs['class'] = 'form-control'
        self.fields['fullName'].widget.attrs['class'] = 'form-control'
        self.fields['totalExp'].widget.attrs['class'] = 'form-control'
        self.fields['currentCTC'].widget.attrs['class'] = 'form-control'
        self.fields['noticePeriod'].widget.attrs['class'] = 'form-control'
        self.fields['relocation'].widget.attrs['class'] = 'form-select'
        # self.fields['relocation'].widget.attrs['data-control'] = 'select2'
        self.fields['whatsapp'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['currentRole'].widget.attrs['class'] = 'form-control'
        self.fields['changeReason'].widget.attrs['class'] = 'form-control'
        self.fields['currentOrganisation'].widget.attrs['class'] = 'form-control'
        self.fields['academicQualification'].widget.attrs['class'] = 'form-control'
        self.fields['technicalCertification'].widget.attrs['class'] = 'form-control'
        self.fields['uploadCV'].widget.attrs['class'] = 'form-control'
        self.fields['uploadCV'].widget.attrs['id'] = 'inputGroupFile'
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = 'Provide Details'


class empCVFormFE(forms.ModelForm):
    class Meta:
        model = empResume
        fields = ('fullName', 'totalExp', 'currentCTC', 'noticePeriod', 'relocation', 'whatsapp',
                  'email', 'currentRole', 'changeReason', 'currentOrganisation', 'academicQualification',
                  'technicalCertification', 'uploadCV')

    def __init__(self, *args, **kwargs):
        super(empCVFormFE, self).__init__(*args, **kwargs)
        self.fields['fullName'].widget.attrs['class'] = 'form-control'
        self.fields['totalExp'].widget.attrs['class'] = 'form-control'
        self.fields['currentCTC'].widget.attrs['class'] = 'form-control'
        self.fields['noticePeriod'].widget.attrs['class'] = 'form-control'
        self.fields['relocation'].widget.attrs['class'] = 'form-select'
        # self.fields['relocation'].widget.attrs['data-control'] = 'select2'
        self.fields['whatsapp'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['currentRole'].widget.attrs['class'] = 'form-control'
        self.fields['changeReason'].widget.attrs['class'] = 'form-control'
        self.fields['currentOrganisation'].widget.attrs['class'] = 'form-control'
        self.fields['academicQualification'].widget.attrs['class'] = 'form-control'
        self.fields['technicalCertification'].widget.attrs['class'] = 'form-control'
        self.fields['uploadCV'].widget.attrs['class'] = 'form-control'
        self.fields['uploadCV'].widget.attrs['id'] = 'inputGroupFile'
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = 'Provide Details'