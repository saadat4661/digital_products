from django.db import models
from django.utils.translation import gettext_lazy as _   # ugettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_(
        'parent'), blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(verbose_name=_('description'), blank=True)
    avatar = models.ImageField(verbose_name=_(
        'avatar'), blank=True, upload_to='categories/')
    is_enable = models.BooleanField(default=True, verbose_name=_('is enable'))
    created_time = models.DateTimeField(
        verbose_name=_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(
        verbose_name=_('updated time'), auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=50)
    description = models.TextField(verbose_name=_('description'), blank=True)
    avatar = models.ImageField(verbose_name=_(
        'avatar'), blank=True, upload_to='products/')
    is_enable = models.BooleanField(default=True, verbose_name=_('is enable'))
    categories = models.ManyToManyField(
        'Category', verbose_name=_('categories'), blank=True)
    created_time = models.DateTimeField(
        verbose_name=_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(
        verbose_name=_('updated time'), auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.title


class File(models.Model):
    FILE_AUDIO = 1
    FILE_VIDEO = 2
    FILE_PDF = 3
    FILE_IMAGE = 4
    FILE_TYPES = (
        (FILE_AUDIO, _('audio')),
        (FILE_VIDEO, _('video')),
        (FILE_PDF, _('pdf')),
        (FILE_IMAGE, _('image'))
    )
    product = models.ForeignKey('Product', verbose_name=_(
        'product'), on_delete=models.CASCADE, related_name='files')
    title = models.CharField(verbose_name=_('title'), max_length=50)
    file = models.FileField(verbose_name=_(
        'file'), upload_to='files/%Y/%m/%d/')
    file_type = models.PositiveSmallIntegerField(
        _('file type'), choices=FILE_TYPES)
    is_enable = models.BooleanField(default=True, verbose_name=_('is enable'))
    created_time = models.DateTimeField(
        verbose_name=_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(
        verbose_name=_('updated time'), auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('File')
        verbose_name_plural = _('Files')
