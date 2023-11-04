from django import forms
from .models import company, jobs


class companyForm(forms.ModelForm):
    class Meta:
        model = company
        fields = ('name', 'profile', 'contact', 'website', 'address', 'logo', 'status')

    def __init__(self, *args, **kwargs):
        super(companyForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['contact'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['website'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-select'
        self.fields['status'].widget.attrs['data-control'] = 'select2'
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = 'Provide Details'


class jobForm(forms.ModelForm):
    class Meta:
        model = jobs
        fields = ('company', 'title', 'experience', 'salary', 'location', 'jd', 'role', 'industry', 'department',
                  'roleCategory', 'empType', 'keySkills', 'education', 'status')

    def __init__(self, *args, **kwargs):
        super(jobForm, self).__init__(*args, **kwargs)
        self.fields['company'].widget.attrs['class'] = 'form-select'
        self.fields['company'].widget.attrs['data-control'] = 'select2'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['experience'].widget.attrs['class'] = 'form-control'
        self.fields['salary'].widget.attrs['class'] = 'form-control'
        self.fields['location'].widget.attrs['class'] = 'form-control'
        self.fields['role'].widget.attrs['class'] = 'form-control'
        self.fields['industry'].widget.attrs['class'] = 'form-control'
        self.fields['department'].widget.attrs['class'] = 'form-control'
        self.fields['roleCategory'].widget.attrs['class'] = 'form-control'
        self.fields['empType'].widget.attrs['class'] = 'form-control'
        self.fields['keySkills'].widget.attrs['class'] = 'form-control'
        self.fields['education'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-select'
        self.fields['status'].widget.attrs['data-control'] = 'select2'
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = 'Provide Details'