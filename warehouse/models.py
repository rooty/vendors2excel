# -*- coding: utf-8 -*-
__author__ = 'rooty'

from django.db import models
from django.conf import settings
import os
import uuid

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


class VendorPriceFile(models.Model):
    """
    Сохранение файлов загруженых прайсов, один файл = загруженый файл прайса от вендора
    """
    #
    """
    генерация уникального имени для файла прайса
    """
    def get_file_path(self, filename):
        extension = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), extension)
        return os.path.join("price", filename)


    vendor = models.ForeignKey(Vendor, related_name='vendorpricefile2vendor', verbose_name='vendor price file')
    pricefile = models.FileField(upload_to=get_file_path, verbose_name='price file name')
    pricedate = models.DateTimeField(verbose_name='price date time')

    class Meta:
        db_table = 'vendorpricefile'

    def __unicode__(self):
        return u"%s от %s" % (self.vendor.name, self.pricedate)



def convertvendorprice2price(sender, instance, created, **kwargs):
    return 1

models.post_save.connect(convertvendorprice2price, sender=VendorPriceFile, dispatch_uid='VendorPriceFile')