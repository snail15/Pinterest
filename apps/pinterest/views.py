# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Pin, Board, Topic
from ..users.models import User
from .forms import PinForm, BoardForm, TopicForm
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Q

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
        return redirect(reverse('pinterest:show_user_pins'))
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
    board_form = BoardForm()

    context = {
        'user': current_user,
        'follower': followers_num,
        'following': following_num,
        'pin_form': pin_form,
        'board_form': board_form

    }
    return render(request, 'pinterest/user_show.html', context)

def logout(request):
    
    del request.session['username']
    del request.session['email']
    return redirect(reverse('users:greeting'))

def show_user_pins(request):
    
    user_pins = Pin.objects.filter(created_by=User.objects.get(email=request.session['email']))
    context = {
        'pins': user_pins
    }
    return render(request, 'pinterest/user_pin.html', context)

def create_topic(request):
    if request.method == 'POST':
        print "CREATING A TOPIC BABY"
        Topic.objects.create(name=request.POST['name'])
        return redirect(request.META.get('HTTP_REFERER', '/'))

# def board_index(request):

def board_index(request):
    user_boards = Board.objects.filter(created_by=User.objects.get(email=request.session['email']))
    context = {
        'boards': user_boards
    }
    return render(request, 'pinterest/board_index.html', context)


def create_board(request):
    
    if request.method == "POST":
            try:
                user = User.objects.get(email=request.session['email'])
                topic = Topic.objects.get(id=request.POST['topic'])
            except Exception as problem:
                return redirect('/')
            try:
                topic = Topic.objects.get(name=request.POST['topic'])
            except:
                topic = Topic.objects.create(name=request.POST['topic'])
            data = {}
            data['title'] = request.POST['title']
            data['description'] = request.POST['description']
            data['created_by'] = user
            data['topic'] = [topic]
            form = BoardForm(data)
            new_board = form.save(commit=False)
            new_board.created_by = user
            new_board.save()
            return redirect(reverse('pinterest:pin_index'))
    elif request.method == "GET":
        form = BoardForm()
        context = {
            'form': form
        }
        return render(request, 'pinterest/create_board.html', context)

# def show_board(request):
def show_board(request, id):
    try:
        board = Board.objects.get(id=id)
    except Exception as problem:
        return redirect(reverse('pinterest:pin_index'))
    context = {
        'board': board,
        'pins': board.pins.all()
    }
    return render(request, 'pinterest/show_board.html', context)


# def edit_board(request):


# def delete_board(request):

def search(request):
    search_term = request.POST.get('search_bar')
    print("#####################################")
    print(search_term)
    searched_pin = Pin.objects.filter(Q(title__contains=search_term) | Q(description__contains=search_term))
    searched_user = User.objects.filter(name__startswith=search_term)
    print(searched_user)
    context = {
        'pins': searched_pin
        # 'users': searched_user
    }
    return render(request, 'pinterest/search_result.html', context)

def user_show_info(request):
    pass