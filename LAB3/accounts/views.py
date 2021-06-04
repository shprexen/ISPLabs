from django.contrib.sites import requests
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import StudentForm, CreateUserForm
from .decorators import unauthenticated_user

import requests


class Lesson:
    def __init__(self, lessonTime="-", subject="-", lessonType="-", employee="-", audience="-"):
        self.lessonTime = lessonTime
        self.subject = subject
        self.lessonType = lessonType
        self.employee = employee
        self.audience = audience


class Exam:
    def __init__(self, lessonTime="-", subject="-", lessonType="-", employee="-", audience="-", datetime="-"):
        self.lessonTime = lessonTime
        self.subject = subject
        self.lessonType = lessonType
        self.employee = employee
        self.audience = audience
        self.datetime = datetime


def get_schedule(schedule):
    if schedule:
        lessons = []
        if not 'schedule' in schedule[0].keys():
            for i in range(len(schedule)):
                if len(schedule[i]['employee']) != 0:
                    lesson = Lesson(schedule[i]['lessonTime'],
                                    schedule[i]['subject'],
                                    schedule[i]['lessonType'],
                                    schedule[i]['employee'][0]['fio'],
                                    schedule[i]['auditory'][0])
                else:
                    lesson = Lesson(schedule[i]['lessonTime'],
                                    schedule[i]['subject'],
                                    schedule[i]['lessonType'], )
                lessons.append(lesson)
        else:
            for i in range(len(schedule)):
                exam = Exam(schedule[i]['schedule'][0]['lessonTime'],
                              schedule[i]['schedule'][0]['subject'],
                              schedule[i]['schedule'][0]['lessonType'],
                              schedule[i]['schedule'][0]['employee'][0]['fio'],
                              schedule[i]['schedule'][0]['auditory'],
                              schedule[i]['weekDay'])
                lessons.append(exam)

        return lessons


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            Student.objects.create(
                user=user
            )
            group = Group.objects.get(name='customer')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('user-page')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def userPage(request):
    response = requests.get('https://journal.bsuir.by/api/v1/studentGroup/schedule?studentGroup=953506')

    schedule = response.json()['todaySchedules']
    tomorrow_schedule = response.json()['tomorrowSchedules']
    exam_schedule = response.json()['examSchedules']

    lessons = get_schedule(schedule)
    tomorrow_lessons = get_schedule(tomorrow_schedule)
    exams = get_schedule(exam_schedule)

    context = {'lessons': lessons,
               'tomorrow_lessons': tomorrow_lessons,
               'exams': exams}

    return render(request, 'accounts/user.html', context)


@login_required(login_url='login')
def accountSettings(request):
    student = request.user.student
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'accounts/account_settings.html', context)
