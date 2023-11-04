import requests
from django.contrib import messages, auth
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import empResume
from .forms import empResumeForm


@login_required(login_url='login')
def empCVList(request):
    allempResumes = empResume.objects.all().order_by('-createdDate')
    context = {
        'allempResumes': allempResumes,
    }
    return render(request, 'back/pages/employee/read.html', context)


@login_required(login_url='login')
def empCVCreate(request):
    empProForm = empResumeForm()
    if request.method == 'POST':
        empProForm = empResumeForm(request.POST, request.FILES)
        if empProForm.is_valid():
            empProForm.save()
            messages.success(request, 'Employee CV has been created.')
            return redirect('empList')
        else:
            messages.error(request, 'Please correct form errors.')

    context = {
        'empProForm': empProForm,
    }
    return render(request, 'back/pages/employee/create.html', context)


@login_required(login_url='login')
def empCVEdit(request, pk):
    empResumes = get_object_or_404(empResume, id=pk)
    empResumesForm = empResumeForm(instance=empResumes)
    if request.method == 'POST':
        empResumesForm = empResumeForm(request.POST, instance=empResumes)
        if empResumesForm.is_valid():
            empResumesForm.save()
            messages.success(request, 'Employee CV has been updated.')
            return redirect('empCVList')
        else:
            messages.error(request, 'Please correct form errors.')

    context = {
        'empResumes': empResumes,
        'empResumesForm': empResumesForm,
    }
    return render(request, 'back/pages/employee/update.html', context)


def empCVDelete(request, pk):
    empCV = get_object_or_404(empResume, id=pk)
    if request.method == "POST":
        empCV.delete()
        return redirect('empList')
    context = {
        'empCV': empCV,
    }
    return render(request, 'back/pages/employee/delete.html', context)