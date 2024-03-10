from django.db import models

CATEGORY_CHOICES = (
    [0, "Jedzenie"],
    [1, "Napoje"],
)


class Product(models.Model):
    name = models.CharField(max_length=32, verbose_name="Nazwa produktu")
    price = models.DecimalField(max_digits=3, decimal_places=2, verbose_name="Cena produktu")
    quantity = models.IntegerField(default=0, verbose_name="Ilosć")
    category = models.IntegerField(choices=CATEGORY_CHOICES, verbose_name="Kategoria")
    description = models.TextField(verbose_name="Opis produktu", null=True, blank=True)

    def __str__(self):
        return self.name
