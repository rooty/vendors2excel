# -*- coding: utf-8 -*-
__author__ = 'rooty'

from django.db import models
from django.conf import settings
class Vendor(models.Model):
    """
    Class Vendors
    """
    # todo: add more funcional
    name = models.CharField(verbose_name='vendor name',max_length=128)
    description = models.TextField(verbose_name='vendor description',blank=True)


    class Meta:
        db_table = 'vendor'
        ordering = ['id','name']


    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        settings.logger.info('Vendor: save...')
        return super(Vendor, self).save(*args, **kwargs)


