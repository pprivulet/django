# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Tailor(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


class Customer(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
