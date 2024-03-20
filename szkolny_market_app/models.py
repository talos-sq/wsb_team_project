from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = (
    [0, "Jedzenie"],
    [1, "Napoje"],
)

CLASSES_YEAR_CHOICES = (
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6],
)

CLASSES_TYPE_CHOICES = (
    [0, "A"],
    [1, "B"],
    [2, "C"],
    [3, "D"],
)


class UserCustomPermissions(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Użytkownik")

    class Meta:
        permissions = (
            ("student", "Is student"),
            ("parent", "Is parent"),
            ("worker", "Is worker"),
        )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Użytkownik")
    class_year = models.IntegerField(choices=CLASSES_YEAR_CHOICES, verbose_name="Klasa")
    class_type = models.IntegerField(choices=CLASSES_TYPE_CHOICES, verbose_name="Klasa")
    balance = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Stan konta")

    class Meta:
        verbose_name = "Uczeń"
        verbose_name_plural = "Uczniowie"

    def __str__(self):
        return f"{self.user.username} - {self.user.first_name} {self.user.last_name}"


class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Parent")
    children = models.ManyToManyField(Student, blank=True, verbose_name="Children")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Product(models.Model):
    name = models.CharField(max_length=32, verbose_name="Nazwa produktu")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Cena produktu")
    quantity = models.IntegerField(default=0, verbose_name="Ilosć")
    category = models.IntegerField(choices=CATEGORY_CHOICES, verbose_name="Kategoria")
    description = models.TextField(verbose_name="Opis produktu", null=True, blank=True)

    def __str__(self):
        return self.name
