# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from django.db import models
from django.conf import settings
from django.core.cache import cache


class Cell(models.Model):
    x = models.IntegerField(verbose_name=u"x")
    y = models.IntegerField(verbose_name=u"y")
    ip = models.CharField(max_length=20, verbose_name=u"IP", null=True, blank=True)
    lock_dt = models.DateTimeField(verbose_name=u"Дата/время блокировки", null=True, blank=True)

    @classmethod
    def get_locks(cls):
        now = datetime.now()
        return dict(((cell.x, cell.y), (cell.lock_dt - now + settings.CELL_LOCK_PERIOD).seconds/60)
                    for cell in Cell.objects.all() if cell.lock_dt >= now - settings.CELL_LOCK_PERIOD
        )

    @classmethod
    def is_locked(cls, x, y):
        try:
            cell = Cell.objects.get(x=x, y=y)
            return cell.lock_dt >= datetime.now() - settings.CELL_LOCK_PERIOD
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
        check = cache.get('lock/%s' % ip)
        if check:
            return False, u"Блокировка не чаще раза в 10 секунд"

        try:
            lock = Lock.objects.get(x=x, y=y, ip=ip)
            if lock.lock_dt < datetime.now() - settings.IP_LOCK_PERIOD:
                return True, u"Можно)"
            else:
                print lock, lock.x, lock.y, lock.ip
                return False, u"Вы сегодня уже блокировали эту картинку"
        except Lock.DoesNotExist:
            return True, u"Можно"

    @classmethod
    def add(cls, x, y, ip):
        cls.objects.create(x=x, y=y, ip=ip, lock_dt=datetime.now())
        cache.set('lock/%s' % ip, True, 10)

    class Meta:
        verbose_name = u"Блокировка"
        verbose_name_plural = u"Блокировки"


