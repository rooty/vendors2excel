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

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        settings.logger.info('Vendor: save...')
        return super(Vendor, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


    class Meta:
        db_table = 'vendor'
        ordering = ['id','name']




class VendorPriceFile(models.Model):
    """
    Сохранение файлов загруженых прайсов, один файл = загруженый файл прайса от вендора
    """

    def get_file_path(self, filename):
        """
        генерация уникального имени для файла прайса
        """
        extension = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), extension)
        return os.path.join("price", filename)


    vendor = models.ForeignKey(Vendor, related_name='vendorpricefile2vendor', verbose_name='vendor price file')
    pricefile = models.FileField(upload_to=get_file_path, verbose_name='price file name')
    pricedate = models.DateTimeField(verbose_name='price date time')
    converted = models.BooleanField(default=False,verbose_name='file converted')

    def __unicode__(self):
        return u"%s от %s" % (self.vendor.name, self.pricedate)


    class Meta:
        db_table = 'vendorpricefile'
        ordering = ['vendor','pricedate']


class   PriceItem(models.Model):
    """
    выходная прайсовая (внутрения) позиция товара
    """
    name = models.CharField(max_length=128,verbose_name='price item')
    description = models.TextField(verbose_name='price item description',blank=True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()

        if self.description == '':
            self.description = self.name

        settings.logger.info('Price Item: save...')
        return super(PriceItem, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


    class Meta:
        db_table = 'priceitem'
        ordering = ['name']



def convertvendorprice2price(sender, instance, created, **kwargs):
    """
    функция конвертации нового загруженного прайса
    """
    vfp = VendorPriceFile(sender)
    if not vfp.converted:
        filename2process = vfp.pricefile.name
        vfp.converted = True
        vfp.save()
    # todo: добавить обработку самого файла(конвертацию)
    #
    return True

models.signals.post_save.connect(convertvendorprice2price, sender=VendorPriceFile, dispatch_uid='VendorPriceFile')