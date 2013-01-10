# -*- coding: utf-8 -*-
__author__ = 'rooty'

from django.db import models

class Vendor(models.Model):
    """Class Vendors"""
    # todo: add more funcional
    name = models.CharField(verbose_name='vendor name',max_length=128)
    description = models.TextField(verbose_name='vendor description',blank=True)

