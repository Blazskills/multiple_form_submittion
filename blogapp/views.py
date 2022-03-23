
# from django.http import HttpResponse
from django.shortcuts import redirect, render

from blogapp.utils import create_activity_stream, generate_digits, update_activity_stream
from .models import ActivityStream, ActivityStreamTarget, Memebers, NewComer
from .forms import UserRegistrationForm, LoginForm, MemebersForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# from django.contrib import messages


# Create your views here.
@login_required(login_url='signin')
def index(request):
    ref_id = generate_digits(15)
    # create_activity_stream(request.user,'New Member Registeration', ref_id, response_status='Attempt')
    if request.method == 'GET':
        print(request)
    elif request.method == 'POST':
        pst = NewComer()
        initial = {}
        name = request.POST.getlist('name')
        email = request.POST.getlist('email')
        phone = request.POST.getlist('phone')
        home_address = request.POST.getlist('home_address')
        contact_via = request.POST.getlist('contact_via')
        invited_by = request.POST.getlist('invited_by')
        intrest = request.POST.getlist('intrest')
        prayer_request = request.POST.getlist('prayer_request')
        observations = request.POST.getlist('observations')
        current_job = request.POST.getlist('current_job')

        bulk_number = request.POST.getlist('hidden_form_number')
        bulk_number = int(bulk_number[0])
        # print(bulk_number)
        
        users_created = []
        user_created_failed = []
        list_member=[]
        failed_count2=None
        

        for i in range(bulk_number):
            list_member.append(i)
            all_post = NewComer.objects.create(
                name=name[i],
                email=email[i],
                phone=phone[i],
                home_address=home_address[i],
                contact_via=contact_via[i],
                invited_by=invited_by[i],
                intrest=intrest[i],
                prayer_request=prayer_request[i],
                observations=observations[i],
                current_job=current_job[i],
            )
            if name[i] == '' or None:
                user_created_failed.append(i)
                continue 
            users_created.append(all_post)
            
            # print(name[i])
            # print(email[i])
        users_count = len(users_created)
        failed_count = len(user_created_failed)
        passed_count= users_count - failed_count
        print(users_count)
        print(failed_count)
       
        # print(f"total passed count {passed_count}")
        all_post.save()
        
        # print(users_count)
    # create_activity_stream(request.user,'New Member Registeration', ref_id, response_status='Attempt')
        create_activity_stream(request.user, f"{users_count} New Comers registered and {failed_count} registration failed",
                               ref_id, 'Success', target=users_created)
        return redirect('home')
    return render(request, 'multForm/index.html')


def register(request):
    ref_id = generate_digits(15)
    # create_activity_stream(
    #     request.user, 'Registration Attempt', ref_id, response_status='Attempt')

    if request.user.is_authenticated:
        return redirect('home')
    form = UserRegistrationForm()
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm = request.POST["confirm"]
        if password == confirm:
            new_user = User.objects.create_user(
                username=username,
                email=email,
                password=password,

            )
            new_user.set_password(password)
            new_user.save()
            # update_activity_stream(ref_id, "Registered",
            #                        'Success', target=new_user)
            return redirect('home')
        # update_activity_stream(ref_id, "Failed Registration", 'Failed')
    context = {
        'form': form
    }
    return render(request, 'multForm/register.html', context)


def signin(request):
    ref_id = generate_digits(15)
    print(ref_id)
    # create_activity_stream(request.user,'New Member Registeration', ref_id, response_status='Attempt')
    # create_activity_stream(request.user, 'Sign In Attempt',
    #                        ref_id, response_status='Attempt')
    # activity_stream_ref_id = str(timezone.now().timestamp()).replace('.', '')
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            create_activity_stream(request.user, f"{user.first_name} {user.last_name} Logged In",
                               ref_id, 'Success', target=user)
            # update_activity_stream(ref_id, "logged In",
            #                        'Success', user=request.user, target=user)
            return redirect('home')
        else:
            context = {
                'form': form,
                'error': 'User not found'
            }
            # update_activity_stream(ref_id, "Failed Login", 'Failed')
            return render(request, 'multForm/login.html', context)
    context = {
        'form': form,
    }
    return render(request, 'multForm/login.html', context)


@login_required(login_url='signin')
def member(request):
    ref_id = generate_digits(15)
    # create_activity_stream(
    #     request.user, 'Attempt Member Registration', ref_id, response_status='Attempt')
    form = MemebersForm()
    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        home_address = request.POST["home_address"]
        contact_via = request.POST["contact_via"]
        memeber_type = request.POST["memeber_type"]
        current_job = request.POST["current_job"]
        if name:
            savemem = Memebers.objects.create(name=name, email=email, phone=phone, home_address=home_address,
                                              contact_via=contact_via, memeber_type=memeber_type, current_job=current_job)
            savemem.save()
            create_activity_stream(request.user, "New Member registered",
                               ref_id, 'Success', target=savemem)
            # update_activity_stream(
            #     ref_id, "Member registered Successfully", 'Success', user=request.user, target=savemem)
            return redirect('home')
        create_activity_stream(request.user, "New Member registered",
                               ref_id, 'Failed')
        # update_activity_stream(
        #     ref_id, "Member registered Failed", 'Failed', user=request.user)
    context = {"form": form}
    return render(request, 'multForm/member.html', context)


@login_required(login_url='signin')
def home(request):
    activitystreams = ActivityStream.objects.all()

    context = {"activitystreams": activitystreams}
    return render(request, 'multForm/home.html', context)


@login_required(login_url='signin')
def activity_stream(request, ref_id):
    active_stream = ActivityStream.objects.filter(ref_id=ref_id)
    active_stream = active_stream[0] if active_stream else None
    activitystreamsets = ActivityStreamTarget.objects.filter(
        activity_stream=active_stream)
    print(activitystreamsets)
    context = {"activitystreamsets": activitystreamsets}
    return render(request, 'multForm/activity_stream_detail.html', context)

@login_required(login_url='signin')
def signout(request):
    ref_id = generate_digits(15)
    create_activity_stream(request.user, f"{request.user.first_name} {request.user.last_name}  Logged Out",
                               ref_id, 'Success', target=request.user)
    # create_activity_stream(request.user, 'Sign out',
    #                        ref_id, response_status='Success')
    logout(request)
    return redirect('register')
