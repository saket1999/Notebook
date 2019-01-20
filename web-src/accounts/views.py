from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.utils.html import strip_tags
from django.contrib import messages
from django.core.validators import validate_email
from django.shortcuts import get_object_or_404


class HomeView(TemplateView):

    def get(self, request):
        context = {'title': 'home'}
        return render(request, 'index.html', context=context)


class LoginView(View):

    def get(self, request):
        return redirect('home')

    def post(self, request):
        if request.method == 'POST':
            username = strip_tags(request.POST.get('username'))
            password = strip_tags(request.POST.get('password'))
            user = authenticate(username=username, password=password)
            if user is not None:
                print('User found')
                login(request, user)
                return redirect('home')
            else:
                print('Non existing user')
                messages.error(request, 'oops! username or password does not exists!')
        context = {'title': 'Home'}
        return render(request, 'index.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('home')


class RegistrationView(View):

    def get(self, request):
        return redirect('home')

    def post(self, request):

        if request.method == 'POST':
            # get user model
            User = get_user_model()

            # clean data
            username = strip_tags(request.POST.get('username'))
            password = strip_tags(request.POST.get('password1'))
            conf_password = strip_tags(request.POST.get('password2'))
            first_name = strip_tags(request.POST.get('first_name'))
            last_name = strip_tags(request.POST.get('last_name'))
            email = strip_tags(request.POST.get('email'))

            error_msg = []

            # check if passwords are identical; if not, raise error
            if password == conf_password:
                pass
            else:
                print(password, conf_password, sep=' is matching to ')
                print('password err')
                error_msg.append('Passwords do not match')

            # check if email is valid; if not, raise error
            if email:
                if validate_email(email) is None:
                    print(validate_email(email))
                    pass
                else:
                    print('email err')
                    error_msg.append('Invalid email')
            else:
                error_msg.append('kindly enter email')

            # check if username is taken and Email are taken
            try:
                user_with_username = User.objects.get(username=username)
            except:
                user_with_username = None
            if user_with_username:
                error_msg.append('Username Already Taken !')

            # check if email is taken
            try:
                user_with_mail = User.objects.get(email=email)
            except:
                user_with_mail = None
            if user_with_mail:
                error_msg.append('Email Already exists!')

            context = {'title': 'error', 'messages': error_msg}

            # if error is raised redirect to home
            if error_msg:
                return render(request, 'index.html', context=context)

            # If No error was raised, Create User
            else:
                try:
                    User = get_user_model()
                    user = User.objects.create(username=username, email=email, first_name=first_name,
                                               last_name=last_name)
                    print('user created')
                    user.set_password(password)
                    user.save()
                    return render(request, 'index.html', context={'messages': ['user created successfully',
                                                                               'Login to continue']})
                except Exception as e:
                    print(e)
                    return render(request, 'index.html', context={'messages': e})


