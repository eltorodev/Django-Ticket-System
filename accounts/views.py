from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login

from accounts.forms import CustomUserCreationForm, UserLoginForm


def user_login(request):
    if request.user.is_authenticated:
        return redirect('ticket:index')
    form = UserLoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return JsonResponse({
                        'status': True,
                        'message': 'Login realizado com sucesso',
                    })
                else:
                    return JsonResponse({
                        'status': False,
                        'message': 'A conta não está ativa',
                    })
            else:
                return JsonResponse({
                    'status': False,
                    'message': 'Usuário e/ou senha incorreto(s)',
                })
        else:
            return JsonResponse({
                'status': False,
                'message': form.errors.as_json(),
            })
    context = {'form': form}
    return render(request, 'accounts/user/login.html', context)


def user_register(request):
    if request.user.is_authenticated:
        return redirect('ticket:index')
    form = CustomUserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = form.save()
            return JsonResponse({
                'status': True,
                'message': f'{username}, cadastrado com sucesso',
            })
        else:
            return JsonResponse({
                'status': False,
                'message': form.errors.as_json(),
            })
    context = {'form': form}
    return render(request, 'accounts/user/register.html', context)
