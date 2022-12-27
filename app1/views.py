from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app1.models import Registration

# Create your views here.


@login_required(login_url='login')
def HomePage(request):
    context = {
        "name": request.user.first_name
    }
    # print("---------------", Registration.objects.get(user=request.user).address)
    return render(request, 'home.html', context)


def SignupPage(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")
        fntxt = request.POST.get("fntxt")
        lntxt = request.POST.get("lntxt")
        address = request.POST.get("address")
        street = request.POST.get("street")
        pincode = request.POST.get("pincode")

        if pass1 != pass2:
            return render(request, 'signup.html', {'alert_flag': True})
        else:
            try:
                User.objects.get(username=uname)
                return render(request, 'signup.html', {'error': True})
            except User.DoesNotExist:
                emlchck = User.objects.filter(email=email)
                if emlchck:
                    return render(request, 'signup.html', {'error1': True})
                else:
                    new_user = User.objects.create_user(
                        username=uname, email=email, password=pass1)
                    new_user.first_name = fntxt
                    new_user.last_name = lntxt
                    new_user.save()

                    user_address = {
                        "address": address,
                        "street": street,
                        "pincode": pincode
                    }

                    new_user1 = Registration.objects.create(
                        user=new_user,
                        **user_address

                    )
                    return redirect('login')
    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == "POST":
        uname1 = request.POST.get('username')
        pass1 = request.POST.get('pass')
        # user_email = User.objects.get(email=uname1).username

        user = authenticate(request, username=uname1, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'alert_flag': True})

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')