# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from django.db import models


class Cell(models.Model):
    x = models.IntegerField(verbose_name=u"x")
    y = models.IntegerField(verbose_name=u"y")
    ip = models.CharField(max_length=20, verbose_name=u"IP", null=True, blank=True)
    lock_dt = models.DateTimeField(verbose_name=u"Дата/время блокировки", null=True, blank=True)

    @classmethod
    def get_locks(cls):
        return dict(((cell.x, cell.y), True) for cell in Cell.objects.all() if cell.lock_dt >= datetime.now() - timedelta(hours=1))

    @classmethod
    def is_locked(cls, x, y):
        try:
            cell = Cell.objects.get(x=x, y=y)
            return cell.lock_dt >= datetime.now() - timedelta(hours=1)
        except Cell.DoesNotExist:
            return False

    @classmethod
    def lock(cls, x, y, ip):
        try:
            cell = Cell.objects.get(x=x, y=y)
        except Cell.DoesNotExist:
            cell = Cell(x=x, y=y)
        cell.ip = ip
        cell.lock_dt = datetime.now()
        cell.save()

    class Meta:
        verbose_name = u"Ячейка"
        verbose_name_plural = u"Ячейки"


class Lock(models.Model):
    x = models.IntegerField(verbose_name=u"x")
    y = models.IntegerField(verbose_name=u"y")
    ip = models.CharField(max_length=20, verbose_name=u"IP")
    lock_dt = models.DateTimeField(verbose_name=u"Дата/время блокировки")

    @classmethod
    def can_lock(cls, x, y, ip):
        try:
            lock = Lock.objects.get(x=x, y=y, ip=ip)
            return lock.lock_dt >= datetime.now() - timedelta(hours=1)
        except Lock.DoesNotExist:
            return True

    @classmethod
    def add(cls, x, y, ip):
        cls.objects.create(x=x, y=y, ip=ip, lock_dt=datetime.now())

    class Meta:
        verbose_name = u"Блокировка"
        verbose_name_plural = u"Блокировки"


