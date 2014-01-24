# -*- coding=utf-8 -*-
from __future__ import print_function

from django.shortcuts import render
from os.path import dirname
import os.path

TEMPLATE_DIR = '{}/templates'.format(dirname(os.path.abspath(__file__)))

def home(request, message):
    args = {'message': message}
    return render(request, '{}/home.djhtml'.format(TEMPLATE_DIR), args)
