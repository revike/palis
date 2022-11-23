from django.db import models

from user.models import User


class Product(models.Model):
    """Таблица продукта"""
    creator_user = models.ForeignKey(User, on_delete=models.PROTECT,
                                     verbose_name='creator')
    vendor_code = models.CharField(max_length=256, verbose_name='vendor_code')
    name = models.CharField(max_length=256, verbose_name='name')
    description = models.TextField(max_length=256, verbose_name='description')
    created = models.DateTimeField(auto_now_add=True, verbose_name='created')
    updated = models.DateTimeField(auto_now=True, verbose_name='updated')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class ProductFile(models.Model):
    """Таблица файлов продукта"""
    product = models.ForeignKey(Product, on_delete=models.PROTECT,
                                verbose_name='prodict_id')
    file = models.FileField(upload_to='product_files', blank=True,
                            verbose_name='product_files')

    def __str__(self):
        return self.product.name

    class Meta:
        db_table = "product_files"
        verbose_name = "Файл продукта"
        verbose_name_plural = "Файлы продуктов"
