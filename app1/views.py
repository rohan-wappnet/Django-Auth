from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from app1.models import Registration

# Create your views here.


@login_required(login_url='login')
def HomePage(request):
    """Function View for home Page"""
    if request.method == "POST":
        # Current user password stored in database
        current_password = request.user.password
        current_password_entered = request.POST.get(
            "currentpass")  # Password entered by user in html
        # New Password entered by user in html
        new_password_1 = request.POST.get("newpass")
        # New Password entered by user in html
        new_password_2 = request.POST.get("confpass")

        # Check password from db and html input
        match_password = check_password(
            current_password_entered, current_password)

        if match_password:

            if new_password_1 == new_password_2:
                user_object = User.objects.get(
                    username=request.user.username)  # User object created
                user_object.set_password(new_password_1)
                user_object.save()
                # Update session to prevent logout
                update_session_auth_hash(request, user_object)

                return render(request, 'home.html', {"updatee": True, "user": request.user,
                                                     "reg": Registration.objects.filter(user=request.user).values})

            else:  # When entered password is not equal to confirm password
                return render(request, 'home.html', {"error": True, "user": request.user,
                                                     "reg": Registration.objects.filter(user=request.user).values})

        else:  # When input password is not equal to user password
            return render(request, 'home.html', {"error1": True, "user": request.user,
                                                 "reg": Registration.objects.filter(user=request.user).values})

    context = {
        "user": request.user,
        "reg": Registration.objects.filter(user=request.user).values
    }
    # print("---------------", Registration.objects.get(user=request.user).address)
    return render(request, 'home.html', context)


def SignupPage(request):
    """Function View for Signup Page"""
    if request.method == "POST":  # Storing all values from html input to variables
        username = request.POST.get("username")
        email = request.POST.get("email")
        password_1 = request.POST.get("password1")
        password_2 = request.POST.get("password2")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        address = request.POST.get("address")
        street = request.POST.get("street")
        pincode = request.POST.get("pincode")
        img = request.FILES['img']

        if password_1 != password_2:  # Comparing both passwords
            return render(request, 'signup.html', {'alert_flag': True})
        else:

            try:
                User.objects.get(username=username)
                return render(request, 'signup.html', {'error': True})

            except User.DoesNotExist:
                email_check = User.objects.filter(email=email)

                if email_check:
                    return render(request, 'signup.html', {'error1': True})

                else:
                    new_user = User.objects.create_user(  # Creating new user object
                        username=username, email=email, password=password_1)
                    new_user.first_name = first_name
                    new_user.last_name = last_name
                    new_user.save()  # Saving data in New user model

                    user_address = {
                        "address": address,
                        "street": street,
                        "pincode": pincode,
                        "image": img
                    }

                    new_user1 = Registration.objects.create(
                        user=new_user,
                        **user_address

                    )
                    return redirect('login')

    return render(request, 'signup.html')


def LoginPage(request):
    """Function View for Login Page"""
    if request.method == "POST":  # Storing all values from html input to variables
        username = request.POST.get('username')
        password = request.POST.get('pass')
        # user_email = User.objects.get(email=uname1).username

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'alert_flag': True})

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def update(request):
    """Function to update User details"""
    if request.method == "POST":  # Stroing all html input to variables
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        address = request.POST.get("address")
        state = request.POST.get("state")
        pincode = request.POST.get("pincode")
        usernamee = request.POST.get("username")
        email = request.POST.get("email")
        try:  # If user doesn't select image, no updates will apply on image
            img = request.FILES['img']
        except:
            img = f"{Registration.objects.get(user=request.user).image}"

        myuser = User.objects.get(pk=request.user.id)  # Creating User object
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.email = email
        myuser.username = usernamee
        myuser.save()

        myuser1 = Registration.objects.get(
            user=request.user)  # Creating Second table Object
        myuser1.address = address
        myuser1.street = state
        myuser1.pincode = pincode
        myuser1.image = img
        myuser1.save()

        # Updating session to prevent logout
        update_session_auth_hash(request, myuser)
        return redirect('home')
