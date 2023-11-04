from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import WebSettings, MailServer, Twilio
from .forms import WebSettingsForm, MailServerForm, TwilioForm



@login_required(login_url='login')
def webSettingsView(request):
    try:
        website_settings = WebSettings.objects.first()
    except WebSettings.DoesNotExist:
        messages.error(request, 'You are not authorised to view this page.')
        return redirect('dashboard')

    if not website_settings:
        if request.method == 'POST':
            ws_form = WebSettingsForm(request.POST, request.FILES)
            if ws_form.is_valid():
                ws_form.save()
                messages.success(request, 'Your settings have been saved.')
                return redirect('webSettings')
        else:
            ws_form = WebSettingsForm()
    else:
        if request.method == 'POST':
            ws_form = WebSettingsForm(request.POST, request.FILES, instance=website_settings)
            if ws_form.is_valid():
                if ws_form.has_changed():
                    ws_form.save()
                    messages.success(request, 'Your settings have been updated.')
                    return redirect('webSettings')
                else:
                    messages.info(request, 'Nothing has changed.')
            else:
                messages.error(request, 'There was an error with your submission. Please check your data.')
        else:
            ws_form = WebSettingsForm(instance=website_settings)

    context = {
        'website_settings': website_settings,
        'ws_form': ws_form,
    }
    return render(request, 'back/pages/settings/webSettingUpdate.html', context)


@login_required(login_url='login')
def mailServerView(request):
    try:
        ms_settings = MailServer.objects.first()
    except MailServer.DoesNotExist:
        messages.error(request, 'You are not authorised to view this page.')
        return redirect('dashboard')

    if request.method == 'POST':
        ms_form = MailServerForm(request.POST, instance=ms_settings)
        if ms_form.is_valid():
            if ms_form.has_changed():
                ms_form.save()
                messages.success(request, 'Your mail server settings has been updated.')
                return redirect('mailServer')
            else:
                messages.info(request, 'Nothing has changed.')
    else:
        ms_form = MailServerForm(instance=ms_settings)

    context = {
        'ms_settings': ms_settings,
        'ms_form': ms_form,
    }
    return render(request, 'be/pages/settings/mailServerUpdate.html', context)


@login_required(login_url='login')
def messagingAPIView(request):
    twilio_settings = Twilio.objects.first()

    if twilio_settings is None:
        if request.method == 'POST':
            msg_form = TwilioForm(request.POST)
            if msg_form.is_valid():
                msg_form.save()
                messages.success(request, 'Your settings have been saved.')
                return redirect('messagingAPI')
            else:
                messages.error(request, 'There was an error in your form.')
        else:
            msg_form = TwilioForm()
    else:
        if request.method == 'POST':
            msg_form = TwilioForm(request.POST, instance=twilio_settings)
            if msg_form.is_valid():
                if msg_form.has_changed():
                    msg_form.save()
                    messages.success(request, 'Your settings have been updated.')
                    return redirect('messagingAPI')
                else:
                    messages.info(request, 'Nothing has changed.')
            else:
                messages.error(request, 'There was an error in your form.')
        else:
            msg_form = TwilioForm(instance=twilio_settings)

    context = {
        'twilio_settings': twilio_settings,
        'msg_form': msg_form,
    }
    return render(request, 'be/pages/settings/messageAPIUpdate.html', context)