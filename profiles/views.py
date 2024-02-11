from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from .forms import CustomUserCreationForm


def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created')

            login(request, user)
            return redirect('edit_profile')

        else:
            messages.success(request, 'An error occurred during registration')

    context = {'page': page, 'form': form}
    return render(request, 'profiles/login_register.html', context)


def user_login(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profile_page')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username OR password is incorrect')
            return render(request, 'profiles/login_register.html')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'You have logged in as {user.username}')
            return redirect('home')
        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'profiles/login_register.html')


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have logged out')
    return redirect('home')


@login_required(login_url="login")
def profile_page(request):
    """
    Renders the profile page
    """

    profile = get_object_or_404(UserProfile, user=request.user)

    return render(
        request,
        'profiles/profile.html',
        {'profile': profile}
    )


@login_required(login_url="login")
def edit_profile(request):
    """
    Renders the edit profile page and handles form submission
    """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile_page')
    else:
        form = UserProfileForm(instance=profile)

    return render(
        request,
        'profiles/edit_profile.html',
        {'form': form}
    )

@login_required(login_url="login")
def delete_profile(request):
    if request.method == 'POST':
        request.user.delete()
        logout(request)
        messages.success(request, 'Your account has been deleted')
        return redirect('home')
    else:
        return redirect('profile_page')