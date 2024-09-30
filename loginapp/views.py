from django.shortcuts import render, redirect
from django.contrib import messages
from loginapp.models import Details

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm-password')

        if password == confirm:
            if Details.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
            else:
                details = Details(name=name, email=email, password=password)
                details.save()
                return redirect('login')
        else:
            messages.info(request,'Password does not match')

    return render(request,'index.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        details = Details.objects.filter(email=email, password=password)
        for x in details:
            print(x)

        if details:
            request.session['email'] = email
            return redirect('profile')
        else:
            messages.info(request,'Please enter a vaild user info')
            return render(request, 'login.html')
    return render(request,'login.html')

def profile(request):
    if 'email' not in request.session:
        return redirect('login')

    if 'email' in request.session:
        email = request.session['email']
        user = Details.objects.get(email=email)

    return render(request,'profile.html',{'user':user})


def logout(request):
    # Check if user is logged in
    if 'email' in request.session:
        # Remove email from session
        del request.session['email']
        request.session.flush()
        messages.success(request, 'You have successfully logged out.')

    return redirect('login')

def edit(request):
    if 'email' in request.session:
        email = request.session['email']
        user = Details.objects.get(email=email)  # Retrieve the current user's details

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if password == confirm:
            # Update the existing user instance with new data
            user.name = name
            user.email = email
            user.password = password
            user.save()  # Save the updated details to the database
            return redirect('profile')
        else:
            messages.info(request, 'Password does not match')

    return render(request, 'edit.html', {'user': user})
