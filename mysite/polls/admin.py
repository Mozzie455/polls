#!/usr/bin/python3

# polls/admin.py

from django.contrib import admin
from .models import Question
# Register your models here.

admin.site.register(Question)