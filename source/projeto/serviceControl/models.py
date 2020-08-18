from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class Ship(models.Model):
    shipName = models.TextField()
    imoNumber = models.IntegerField()
    def __str__(self):
        return self.shipName

class Client(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name

class Factory(models.Model):#usina
    name = models.TextField()    
    def __str__(self):
        return self.name

class Seaport(models.Model):
    name = models.TextField()
    country = models.TextField()
    def __str__(self):
        return self.name+"-"+self.country        

class Service(models.Model):
    ship        = models.ForeignKey(Ship, on_delete=models.CASCADE)
    packing     = models.ForeignKey(Seaport, on_delete=models.CASCADE,related_name='packing')  
    destiny     = models.ForeignKey(Seaport, on_delete=models.CASCADE,related_name='destiny')
    factory     = models.ForeignKey(Factory, on_delete=models.CASCADE)#unsina
    client      =  models.ForeignKey(Client, on_delete=models.CASCADE)
    serviceType = models.TextField()#tipo do serviço
    salesOrder  = models.TextField()
    budgetedAmount = models.TextField()#valor orçado
    month       = models.PositiveIntegerField(default=10,validators=[MinValueValidator(1), MaxValueValidator(12)])
    year        = models.PositiveIntegerField(validators=[MinValueValidator(2019), MaxValueValidator(2500)])
    def __str__(self):
        return str(self.ship)+" ][ "+str(self.packing)+" ][ "+str(self.destiny)
