from django.db import models

class People(models.Model):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=200)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "People"

class Coffee(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='coffee_images/', blank=True, null=True)
    owner = models.ForeignKey(People, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Coffees"