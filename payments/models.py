from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.validators import validate_phone_number

class Gateway(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='gateways/')
    is_enable = models.BooleanField(_('is enable'), default=True)
    # credentials = models.TextField(_('credentials'), blank=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'gateway'
        verbose_name = _('gateway')
        verbose_name_plural = _('gateways')

class Payment(models.Model):
    STATUS_VOID = 0
    STATUS_PAID = 10
    STATUS_ERROR = 20
    STATUS_CANCELED = 30
    STATUS_REFOUNDED = 31

    STATUS_CHOICES = (
        (STATUS_VOID, _('Void')),
        (STATUS_PAID, _('Paid')),
        (STATUS_ERROR, _('Error')),
        (STATUS_CANCELED, _('Canceled')),
        (STATUS_REFOUNDED, _('Refounded')),
    )

    STATUS_TRANSLATIONS = {
        STATUS_VOID:_('Payment could not be processed'),
        STATUS_PAID:_('Payment successful'),
        STATUS_ERROR:_('Payment has encountered an error. Our technical team will check the problem.'),
        STATUS_CANCELED:_('Payment was canceled by the user'),
        STATUS_REFOUNDED:_('This payment has been refounded'),
    }

    user = models.ForeignKey('users.User',verbose_name=_('user'), related_name='%(class)s', on_delete=models.CASCADE)
    package = models.ForeignKey('subscriptions.Package', verbose_name=_('package'), related_name= '%(class)s', on_delete=models.CASCADE)
    gateway = models.ForeignKey(Gateway, verbose_name=_('geteway'), related_name= '%(class)s', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(_('price'), default=0)
    status = models.PositiveSmallIntegerField(_('status'), choices=STATUS_CHOICES, default=STATUS_VOID, db_index=True)
    device_uuid = models.CharField(_('device uuid'), max_length=40, blank=True)
    token = models.CharField(max_length=50)
    phone_number = models.BigIntegerField(_('phone number'), validators=[validate_phone_number], db_index=True)
    consumed_code = models.PositiveIntegerField(_('consumed reference code'), null=True, db_index=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('modification time'), auto_now=True)

    class Meta:
        db_table = 'payment'
        verbose_name = _('payment')
        verbose_name_plural = _('payments')
