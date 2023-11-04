from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import company, jobs
from .forms import companyForm, jobForm


@login_required(login_url='login')
def companyList(request):
    allCompany = company.objects.all().order_by('-createdDate')
    context = {
        'allCompany': allCompany,
    }
    return render(request, 'back/pages/employer/company/read.html', context)


@login_required(login_url='login')
def companyCreate(request):
    compForm = companyForm()
    if request.method == 'POST':
        compForm = companyForm(request.POST, request.FILES)
        if compForm.is_valid():
            compForm.save()
            messages.success(request, 'Employee Profile has been created.')
            return redirect('companyList')
        else:
            messages.error(request, 'Please correct form errors.')

    context = {
        'compForm': compForm,
    }
    return render(request, 'back/pages/employer/company/create.html', context)


@login_required(login_url='login')
def companyEdit(request, pk):
    singleCompany = get_object_or_404(company, id=pk)
    compForm = companyForm(instance=singleCompany)
    if request.method == 'POST':
        compForm = companyForm(request.POST, instance=singleCompany)
        if compForm.is_valid():
            compForm.save()
            messages.success(request, 'Company Profile has been updated.')
            return redirect('companyList')
        else:
            messages.error(request, 'Please correct form errors.')

    context = {
        'singleCompany': singleCompany,
        'compForm': compForm,
    }
    return render(request, 'back/pages/employer/company/update.html', context)


def companyDelete(request, pk):
    compPro = get_object_or_404(company, id=pk)
    if request.method == "POST":
        compPro.delete()
        return redirect('companyList')
    context = {
        'compPro': compPro,
    }
    return render(request, 'back/pages/employer/company/delete.html', context)



@login_required(login_url='login')
def jobList(request):
    allJobs = jobs.objects.all().order_by('-createdDate')
    context = {
        'allJobs': allJobs,
    }
    return render(request, 'back/pages/employer/jobs/read.html', context)


@login_required(login_url='login')
def jobCreate(request):
    if request.method == 'POST':
        jobsForm = jobForm(request.POST, request.FILES)
        if jobsForm.is_valid():
            jobsForm.save()
            messages.success(request, 'Job has been created.')
            return redirect('jobList')
        else:
            messages.error(request, 'Please correct form errors.')
    else:
        jobsForm = jobForm()

    context = {
        'jobsForm': jobsForm,
    }
    return render(request, 'back/pages/employer/jobs/create.html', context)


@login_required(login_url='login')
def jobEdit(request, pk):
    singleJob = get_object_or_404(jobs, id=pk)
    if request.method == 'POST':
        jobsForm = jobForm(request.POST, instance=singleJob)
        if jobsForm.is_valid():
            jobsForm.save()
            messages.success(request, 'Job Details has been updated.')
            return redirect('jobList')
        else:
            messages.error(request, 'Please correct form errors.')
    else:
        jobsForm = jobForm(instance=singleJob)

    context = {
        'singleJob': singleJob,
        'jobsForm': jobsForm,
    }
    return render(request, 'back/pages/employer/jobs/update.html', context)


def jobDelete(request, pk):
    singleJob = get_object_or_404(jobs, id=pk)
    if request.method == "POST":
        singleJob.delete()
        return redirect('jobList')
    context = {
        'singleJob': singleJob,
    }
    return render(request, 'back/pages/employer/jobs/delete.html', context)