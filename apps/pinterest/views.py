# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Pin, Board, Topic
from ..users.models import User
from .forms import PinForm, BoardForm, TopicForm
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    return render(request, 'pinterest/index.html')


def pin_index(request):
    pins = Pin.objects.all()
    context = {
        'pins': pins
    }
    return render(request, 'pinterest/pin_index.html', context)


def create_pin(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.session['email'])
            topic = Topic.objects.get(id=request.POST['topic'])
        except Exception as problem:
            return redirect('/')
        data = {}
        data['title'] = request.POST['title']
        data['description'] = request.POST['description']
        data['image'] = request.FILES['image']
        data['topic'] = [topic]
        data['created_by'] = user
        form = PinForm(data)
        print form
        new_pin = form.save(commit=False)
        new_pin.image = request.FILES['image']
        new_pin.created_by = user
        new_pin.save()
        return redirect(reverse('pinterest:pin_index'))
    elif request.method == "GET":
        form = PinForm()
        topicForm = TopicForm()
        context = {
            'form': form,
            'topicForm': topicForm
        }
        return render(request, 'pinterest/create_pin.html', context)


def show_pin(request, id):
    try:
        pin = Pin.objects.find(id=id)
    except Exception as problem:
        return redirect('/')
    context = {
        'pin': pin
    }
    return render(request, 'pinterest/show_pin.html', context)


def edit_pin(request, id):
    try:
        pin = Pin.objects.find(id=id)
        context = {
            'pin': pin
        }
    except Exception as problem:
        return redirect('/')
    if request.method == "POST":
        return redirect('/')
    elif request.method == "GET":
        return render(request, 'pinterest/edit_pin.html', context)


def delete_pin(request, id):
    try:
        pin = Pin.objects.find(id=id)
        context = {
            'pin': pin
        }
    except Exception as problem:
        return redirect('/')
    if request.method == "POST":
        return redirect('/')
    elif request.method == "GET":
        return render(request, 'pinterest/delete_pin.html', context)

def user_show(request):
   
    current_user = User.objects.filter(email=request.session['email'])
    print(current_user)
    following = current_user[0].following.all()
    following_num = len(following)
    
    followers = current_user[0].followers.all()
    followers_num = len(followers)

    pin_form = PinForm()

    context = {
        'user': current_user,
        'follower': followers_num,
        'following': following_num,
        'pin_form': pin_form

    }
    return render(request, 'pinterest/user_show.html', context)

def logout(request):
    del request.session['username']
    del request.session['email']
    return redirect(reverse('users:greeting'))

def create_topic(request):
    if request.method == 'POST':
        print "CREATING A TOPIC BABY"
        Topic.objects.create(name=request.POST['name'])
        return redirect(request.META.get('HTTP_REFERER', '/'))

# def board_index(request):


# def create_board(request):


# def show_board(request):


# def edit_board(request):


# def delete_board(request):
