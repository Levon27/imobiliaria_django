from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Imovel (models.Model):
    proprietario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.IntegerField() # 0 -> casa    1 -> apartamento
    n_dormitorios = models.IntegerField()
    area = models.IntegerField() #em metros quadrados
    valor = models.DecimalField(max_digits=11,decimal_places=2) #valor máximo: R$ 99.999.999,99
    alugado = models.BooleanField()
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.endereço} {self.area} m²'
    '''
    implementar depois :
    -fotos do imóvel
    -endereço
    '''
