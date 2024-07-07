from django.db import models


class TableType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Table(models.Model):
    table_number = models.PositiveIntegerField()
    table_type = models.ForeignKey(TableType, on_delete=models.CASCADE)
    price = models.FloatField()
    is_available = models.BooleanField(default=True)
    table_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"Table {self.table_number} - {self.table_type}"
