from django.db import models


class Product(models.Model):
    nameprod = models.CharField(max_length=40)
    price = models.CharField(max_length=10)

    def __str__(self):
        return f"Producto: {self.nameprod} - Precio ${self.price}"


class Client(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return f"Cliente Apellido y Nombre: {self.name} {self.last_name} -- e-mail: {self.email}"


class Question(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    email = models.EmailField()
    question = models.CharField(max_length=150)

    def __str__(self):
        return f"Consulta: {self.question} - Datos de contacto: {self.name} - {self.phone} - {self.email}"
