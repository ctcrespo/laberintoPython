#!/usr/bin/python
#-*- coding: utf-8 -*-

from Bomba import Bomba
from Decorator import Decorator

class Bomba(Bomba, Decorator):
    def __init__(self):
        self.activa = None

