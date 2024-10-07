from django.db import models

# Create your models here.


class Dependence(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Business(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    dependences = models.ManyToManyField(Dependence, through='BusinessDependence')  # Relación muchos a muchos
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class BusinessDependence(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    dependence = models.ForeignKey(Dependence, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.business.name} - {self.dependence.name}"