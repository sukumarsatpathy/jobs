import requests
from django.contrib import auth
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Account
from .forms import RegistrationForm, AccountForm, AccountAddForm
from employee.models import empResume
from employer.models import jobs
# Verfication Email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                               username=username, password=password)
            user.save()
            messages.success(request, 'Registration Successful - To activate your account click on the link received in your email.')

            # USER ACTIVATION
            current_site = get_current_site(request)
            mail_subject = 'Please activate your account'
            message_content = {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            }
            html_content = render_to_string('front/accounts/emails/account_verification_email.html', message_content)
            from_email = 'Hireglobal <settings.DEFAULT_FROM_EMAIL>'
            to_email = (email,)
            send_mail(mail_subject, None, from_email, to_email, html_message=html_content)

            return redirect('/accounts/login/?command=verification&email=' + email)

    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'front/accounts/register.html', context)


def login(request):
    current_user = request.user
    if current_user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(email=email, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'You are now logged in.')
                url = request.META.get('HTTP_REFERER')
                try:
                    query = requests.utils.urlparse(url).query
                    params = dict(x.split('=') for x in query.split('&'))
                    if 'next' in params:
                        nextPage = params['next']
                        return redirect(nextPage)
                except:
                    return redirect('dashboard')
            else:
                messages.error(request, 'Invalid login credentials')
                return redirect('login')
        return render(request, 'front/accounts/login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out successfully.')
    return redirect('login')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)

    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated.')
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation Link.')
        return redirect('register')


def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)
            # Forgot Password Email
            current_site = get_current_site(request)
            mail_subject = 'Reset your Password'
            message_content = {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            }
            html_content = render_to_string('front/accounts/emails/reset_password_email.html', message_content)
            from_email = 'Hireglobal <settings.DEFAULT_FROM_EMAIL>'
            to_email = (email,)
            send_mail(mail_subject, None, from_email, to_email, html_message=html_content)
            messages.success(request, 'Password Reset Email has been sent to your email address.')
            return redirect('login')
        else:
            messages.error(request, 'Account doesn\'t Exists!')
            return redirect('forgotPassword')
    return render(request, 'front/accounts/forgotPassword.html')


def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)

    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please Reset your password.')
        return redirect('resetPassword')
    else:
        messages.error(request, 'This link has been expired.')
        return redirect('login')


def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password changed successfully!')
            return redirect('login')
        else:
            messages.error(request, 'Passwords don\'t match.')
            return redirect('resetPassword')
    else:
        return render(request, 'front/pages/accounts/resetPassword.html')


@login_required(login_url='login')
def dashboard(request):
    allCVs = empResume.objects.all().order_by('-createdDate')[0:5]
    allJobs = jobs.objects.all().order_by('-createdDate')[0:5]
    context = {
        'allCVs': allCVs,
        'allJobs': allJobs,
    }
    return render(request, 'back/pages/dashboard.html', context)


@login_required(login_url='login')
def userList(request):
    allUsers = Account.objects.all().order_by('-date_joined')
    context = {
        'allUsers': allUsers,
    }
    return render(request, 'back/pages/users/read.html', context)


@login_required(login_url='login')
def userAdd(request):
    if request.method == 'POST':
        userForm = AccountAddForm(request.POST, request.FILES)
        if userForm.is_valid():
            first_name = userForm.cleaned_data['first_name']
            last_name = userForm.cleaned_data['last_name']
            email = userForm.cleaned_data['email']
            password = userForm.cleaned_data['password']
            contact = userForm.cleaned_data['contact']
            image = userForm.cleaned_data['image']
            is_active = userForm.cleaned_data['is_active']
            username = email.split("@")[0]
            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password,
            )
            user.contact = contact
            user.image = image
            user.is_active = is_active
            user.save()
            messages.success(request, 'Your account has been created.')
            return redirect('userList')
        else:
            messages.error(request, 'Please correct form errors.')
    else:
        userForm = AccountAddForm()

    context = {
        'userForm': userForm,
    }
    return render(request, 'back/pages/users/create.html', context)


@login_required(login_url='login')
def userEdit(request, pk):
    userAccount = get_object_or_404(Account, id=pk)
    userForm = AccountForm(instance=userAccount)
    if request.method == 'POST':
        userForm = AccountForm(request.POST, request.FILES, instance=userAccount)
        if userForm.is_valid():
            userForm.save()
            messages.success(request, 'User account has been updated.')
            return redirect('userList')
        else:
            messages.error(request, 'Please correct form errors.')

    context = {
        'userAccount': userAccount,
        'userForm': userForm,
    }
    return render(request, 'back/pages/users/update.html', context)


def userDelete(request, pk):
    userAccount = get_object_or_404(Account, id=pk)
    if request.method == "POST":
        userAccount.delete()
        return redirect('userList')
    context = {
        'userAccount': userAccount,
    }
    return render(request, 'back/pages/users/delete.html', context)