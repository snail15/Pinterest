# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.

class Following(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#Uer validation class
class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if 'password' in postData:
            if len(postData["password"]) < 5:
                errors["password"] = "Password too short"
        if 'email' in postData:
            if len(postData["email"]) < 1:
                errors['email_error'] = "Enter Your Email"
            elif not EMAIL_REGEX.match(postData['email']):
                errors['invalid_email'] = 'Email Invalid Format'
        if 'fullname' in postData:
            if len(postData['fullname']) < 4:
                errors['name_error'] = "Nmae too short"
        if 'age' in postData:
            if postData['age'] < 1:
                errors['age_error'] = 'Too young'
        return errors

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.IntegerField()
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    followings = models.ManyToManyField(Following, related_name='followers')
    objects = UserManager()

