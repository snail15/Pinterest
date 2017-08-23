# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Pin, Board
from ..users.models import User
from .forms import PinForm, BoardForm
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
        except Exception as problem:
            return redirect('/')
        data = {}
        data['title'] = request.POST['title']
        data['description'] = request.POST['description']
        data['image'] = request.FILES['image']
        data['created_by'] = user
        form = PinForm(data)
        new_pin = form.save(commit=False)
        new_pin.created_by = user
        new_pin.save()
        return redirect('pinterest/pins/')
    elif request.method == "GET":
        form = PinForm()
        context = {
            'form': form
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
    

# def board_index(request):


# def create_board(request):


# def show_board(request):


# def edit_board(request):


# def delete_board(request):
