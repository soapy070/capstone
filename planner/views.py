"""Importing necessary modules: This section imports the required modules such as
HttpResponseRedirect, render, get_object_or_404, reverse, modelform_factory,
and several other modules from Django framework."""
from django.shortcuts import render, get_object_or_404, redirect
from .models import Manager, Member, Team, Location
from django.forms import modelform_factory
from django.forms.widgets import DateInput
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

"""Defining manager_detail, member_detail, team_detail, location_detail,
manager_list, and location_list views: These views retrieve data from the
database using the get_object_or_404 function and render the corresponding HTML templates."""


@login_required(login_url='/templates/login/')
def manager_detail(request, id):
    manager = get_object_or_404(Manager, pk=id)
    return render(request, "manager/manager.html", {"manager": manager})


@login_required(login_url='/templates/login/')
def member_detail(request, id):
    member = get_object_or_404(Member, pk=id)
    return render(request, "member/member.html", {"member": member})


@login_required(login_url='/templates/login/')
def team_detail(request, id):
    team = get_object_or_404(Team, pk=id)
    return render(request, "team/team.html", {"team": team})


@login_required(login_url='/templates/login/')
def location_detail(request, id):
    location = get_object_or_404(Location, pk=id)
    return render(request, "location/location.html", {"location": location})


@login_required(login_url='/templates/login/')
def manager_list(request):
    return render(request, "manager/manager_list.html",
                  {"manager": Manager.objects.all()})


@login_required(login_url='/templates/login/')
def location_list(request):
    return render(request, "location/location_list.html",
                  {"location": Location.objects.all()})


"""MemberForm, LocationForm, ManagerForm & TeamForm: 
These are Django ModelForm classes for the Member and Location models."""
MemberForm = modelform_factory(Member, exclude=[], widgets={'start_date': DateInput(attrs={'type': 'date'})})


"""new_member, update_member, and delete_member views:
These views handle the creation, updating, and deletion of Member
objects. They use the MemberForm class for rendering forms."""


@login_required(login_url='/templates/login/')
def new_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MemberForm()
    return render(request, "member/new_member.html", {"form": form, "date_input_type": "date"})


def update_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MemberForm(instance=member)
    return render(request, "member/update_member.html",
                  {"form": form, "date_input_type": "date", "member_id": member_id})


def delete_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == "POST":
        member.delete()
        return redirect("welcome")
    return render(request, "member/delete_member.html", {"member": member})


LocationForm = modelform_factory(Location, exclude=[])

"""new_location, update_location, and delete_location views: These views handle
the creation, updating, and deletion of Location objects, respectively.
They use the LocationForm class for rendering forms."""


@login_required(login_url='/templates/login/')
@user_passes_test(lambda u: u.is_superuser)
def new_location(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = LocationForm()
    return render(request, "location/new_location.html", {"form": form})


def update_location(request, location_id):
    location = get_object_or_404(Location, id=location_id)
    if request.method == "POST":
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = LocationForm(instance=location)
    return render(request, "location/update_location.html",
                  {"form": form, "date_input_type": "date", "location_id": location_id})


def delete_location(request, location_id):
    location = get_object_or_404(Location, id=location_id)
    if request.method == "POST":
        location.delete()
        return redirect("welcome")
    return render(request, "location/delete_location.html", {"location": location})


ManagerForm = modelform_factory(Manager, exclude=[], widgets={'start_date': DateInput(attrs={'type': 'date'})})

"""new_manager, update_manager, and delete_manager views: These views handle the creation,
updating, and deletion of Manager objects, respectively. They use the ManagerForm class for rendering forms."""


@login_required(login_url='/templates/login/')
@user_passes_test(lambda u: u.is_superuser)
def new_manager(request):
    if request.method == "POST":
        form = ManagerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = ManagerForm()
    return render(request, "manager/new_manager.html", {"form": form})


def update_manager(request, manager_id):
    manager = get_object_or_404(Manager, id=manager_id)
    if request.method == "POST":
        form = ManagerForm(request.POST, instance=manager)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = ManagerForm(instance=manager)
    return render(request, "manager/update_manager.html",
                  {"form": form, "date_input_type": "date", "manager_id": manager_id})


def delete_manager(request, manager_id):
    manager = get_object_or_404(Manager, id=manager_id)
    if request.method == "POST":
        manager.delete()
        return redirect("welcome")
    return render(request, "manager/delete_manager.html", {"manager": manager})


TeamForm = modelform_factory(Team, exclude=[])

"""new_team, update_team, and delete_team views: These views handle the creation,
updating, and deletion of Team objects, respectively. They use the TeamForm class for rendering forms."""


@login_required(login_url='/templates/login/')
def new_team(request):
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = TeamForm()
    return render(request, "team/new_team.html", {"form": form})


def update_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.method == "POST":
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = TeamForm(instance=team)
    return render(request, "team/update_team.html",
                  {"form": form, "team_id": team_id})


def delete_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.method == "POST":
        team.delete()
        return redirect("welcome")
    return render(request, "team/delete_team.html", {"team": team})


"""create_member and create_admin views: These views handle
the creation of new User objects for regular users and administrators."""


@login_required(login_url='/templates/login/')
def create_member(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = UserCreationForm()
    return render(request, "create_member/create_member.html", {'form': form})


@login_required(login_url='/templates/login/')
@user_passes_test(lambda u: u.is_superuser)
def create_admin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = UserCreationForm()
    return render(request, "create_admin/create_admin.html", {'form': form})


"""login_view and logout_view views: These views handle user authentication and logging out."""


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("welcome")
    else:
        form = AuthenticationForm()
    return render(request, "login/login.html", {'form': form})


def logout_view(request):
    logout(request)
    return redirect("welcome")
