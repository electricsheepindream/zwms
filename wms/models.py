from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class BaseModel(models.Model):
    code = models.CharField(max_length=16)
    name = models.CharField(max_length=32)
    crt_time = models.DateTimeField(auto_now=True)
    mod_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Item(BaseModel):
    main_cat = models.CharField(max_length=16)
    produce_cat = models.CharField(max_length=16)
    unit_name = models.CharField(max_length=8)
    sell_cat = models.CharField(max_length=16)
    safe_num = models.IntegerField()
    specs = models.CharField()
    next_product = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class StorageItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    batch_num = models.CharField(max_length=64)
    num = models.FloatField()
    material_cost = models.FloatField()
    gain_way = models.CharField(max_length=8)
    safe_date = models.IntegerField(max_length=8)
    expiry_date = models.DateTimeField()
    warehouse = models.IntegerField()

    def __str__(self):
        return self.item.name


class Bom(BaseModel):
    item = models.OneToOneField(Item, on_delete=models.PROTECT)
    note = models.CharField(max_length=128)


class BomDetailItem(models.Model):
    bom = models.ForeignKey(Bom, on_delete=models.CASCADE)
    item = models.IntegerField()
    num = models.FloatField()


class Warehouse(BaseModel):
    addr = models.CharField(max_length=64)


class WhPart(BaseModel):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)


# class ItemCreateLog(models.Model):
#