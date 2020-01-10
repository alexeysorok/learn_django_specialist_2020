from django.db import models


# TODO:  add default 0 value for quantity


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255, unique=True)
    article = models.CharField(max_length=16, null=True, blank=True, unique=True)
    description = models.TextField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0, blank=True)
    group = models.ForeignKey('products.Group', on_delete=models.PROTECT, null=True)
    tags = models.ManyToManyField('products.Tag')

    def __str__(self):
        if self.article is None:
            return '(---)'.format(self.title)
        else:
            return f"({self.article}) {self.title}"


class Group(models.Model):
    title = models.CharField(max_length=128, unique=True)
    code = models.CharField(max_length=16, unique=True)
    skoro = models.NullBooleanField()

    @property
    def full_title(self):
        return f"({self.code}) {self.title}"

    def __str__(self):
        return self.full_title


class Tag(models.Model):
    title = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return f"{self.title}"
