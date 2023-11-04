from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.contrib import messages
from employer.models import company, jobs
from employee.forms import empResumeForm, empCVFormFE
from employee.models import empResume

# Email
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail


def home(request):
    allCompanies = company.objects.filter(status='Published').order_by('-modifiedDate').annotate(
        jobs_count=Count('jobs'))
    allJobs = jobs.objects.filter(status='Published').order_by('-modifiedDate')
    context = {
        'allCompanies': allCompanies,
        'allJobs': allJobs,
    }
    return render(request, 'front/pages/home.html', context)


def about(request):
    context = {}
    return render(request, 'front/pages/about.html', context)


def jobList(request):
    allJobs = jobs.objects.filter(status='Published').order_by('-createdDate')
    context = {
        'allJobs': allJobs,
    }
    return render(request, 'front/pages/jobList.html', context)


def jobsDetail(request, pk):
    singleJobDetail = get_object_or_404(jobs, id=pk)
    otherJobs = jobs.objects.filter(company=singleJobDetail.company).exclude(id=pk).order_by('-createdDate')
    if request.method == 'POST':
        empResumesForm = empCVFormFE(request.POST, request.FILES)
        if empResumesForm.is_valid():
            positionAppliedFor = singleJobDetail.title
            fullName = empResumesForm.cleaned_data['fullName']
            totalExp = empResumesForm.cleaned_data['totalExp']
            currentCTC = empResumesForm.cleaned_data['currentCTC']
            noticePeriod = empResumesForm.cleaned_data['noticePeriod']
            relocation = empResumesForm.cleaned_data['relocation']
            whatsapp = empResumesForm.cleaned_data['whatsapp']
            email = empResumesForm.cleaned_data['email']
            currentRole = empResumesForm.cleaned_data['currentRole']
            changeReason = empResumesForm.cleaned_data['changeReason']
            currentOrganisation = empResumesForm.cleaned_data['currentOrganisation']
            academicQualification = empResumesForm.cleaned_data['academicQualification']
            technicalCertification = empResumesForm.cleaned_data['technicalCertification']
            uploadCV = empResumesForm.cleaned_data['uploadCV']
            empCV = empResume.objects.create(
                fullName=fullName,
                totalExp=totalExp,
                currentCTC=currentCTC,
                noticePeriod=noticePeriod,
                relocation=relocation,
                whatsapp=whatsapp,
                email=email,
                currentRole=currentRole,
                changeReason=changeReason,
                currentOrganisation=currentOrganisation,
                academicQualification=academicQualification,
                technicalCertification=technicalCertification,
                uploadCV=uploadCV,
            )
            empCV.positionAppliedFor = positionAppliedFor
            empCV.save()

            messages.success(request, 'Successfully applied for the job.')
            mail_subject = fullName + ' submitted CV for ' + positionAppliedFor
            message_content = {
                'fullname': fullName,
                'singleJobDetail': singleJobDetail,
            }
            html_content = render_to_string('front/email/cv-submission-email.html', message_content)
            from_email = 'Hireglobal <settings.DEFAULT_FROM_EMAIL>'
            to_email = ('Hireglobal <sukumarsatpathy@gmail.com>',)
            send_mail(mail_subject, None, from_email, to_email, html_message=html_content)
            return redirect('/')
            # # return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/')
    else:
        empResumesForm = empCVFormFE()

    context = {
        'singleJobDetail': singleJobDetail,
        'otherJobs': otherJobs,
        'empResumesForm': empResumesForm,
    }
    return render(request, 'front/pages/jobDetail.html', context)
