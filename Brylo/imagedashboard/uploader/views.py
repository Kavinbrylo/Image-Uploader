from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile,ImageUpload
from .forms import RegisterForm,ImageUploadForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.shortcuts import get_object_or_404

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password != confirm_password:
                messages.error(request, "Passwords do not match!")
                return redirect('register')

            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, "Registered successfully!")
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'uploader/register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if 'remember_me' in request.POST:
                request.session.set_expiry(604800)  # 7 days in seconds
            else:
                request.session.set_expiry(0)  # expires on browser close

            return redirect('home')
        else:
            return render(request, 'uploader/login.html', {'error': 'Invalid credentials'})

    return render(request, 'uploader/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')
@never_cache
@login_required(login_url='login')
def home(request):
    images = ImageUpload.objects.filter(user=request.user)
    return render(request, 'uploader/home.html', {'images': images})

@never_cache
@login_required(login_url='login')
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save(commit=False)
            image_instance.user = request.user
            image_instance.save()
            return redirect('home')  # After upload, go to home
    else:
        form = ImageUploadForm()
    return render(request, 'uploader/upload.html', {'form': form})

@login_required(login_url='login')
def delete_image(request, image_id):
    image = get_object_or_404(ImageUpload, id=image_id, user=request.user)
    image.delete()
    return redirect('home')

def edit_image(request, image_id):
    image = get_object_or_404(ImageUpload, id=image_id, user=request.user)
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageUploadForm(instance=image)
    return render(request, 'uploader/edit_image.html', {'form': form})