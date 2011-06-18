# -*- coding: utf-8 -*-

from django.db import models


class Cell(models.Model):
    ip = models.CharField(max_length=20, verbose_name=u"IP")
    lock_dt = models.DateTimeField(verbose_name=u"Дата/время блокировки", null=True, blank=True)

    class Meta:
        verbose_name = u"Ячейка"
        verbose_name_plural = u"Ячейки"


class Lock(models.Model):
    ip = models.CharField(max_length=20, verbose_name=u"IP")
    lock_dt = models.DateTimeField(verbose_name=u"Дата/время блокировки")
    cell = models.ForeignKey(Cell, verbose_name=u"Ячейка")

    class Meta:
        verbose_name = u"Блокировка"
        verbose_name_plural = u"Блокировки"


