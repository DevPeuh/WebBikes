from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150) # Nome que vai ser exibido na tela

    def __str__(self): # Retorna o nome da marca
        return self.name

class Bike(models.Model): # models.model serve para criar uma tabela no banco de dados, cada classe representa uma tabela e cada atributo representa uma coluna da tabela
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=100) # Modelo do moto
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='bike_brands') # vai fazer a relação com a tabela Brand, ter proteção para não exluir a marca.
    factory_year = models.IntegerField(blank=True, null=True) # Ano de fabricação podendo ser nulo
    model_year = models.IntegerField(blank=True, null=True) # Ano do modelo podendo ser nulo
    plate = models.CharField(max_length=10, blank=True, null=True) # Placa da moto podendo ser nulo
    value = models.FloatField(blank=True, null=True) # Valor da moto podendo ser nulo
    photo = models.ImageField(upload_to='bikes/', blank=True, null=True) # Foto da moto salva no diretório bikes
    

    def __str__(self): # Retorna o modelo da moto
        return self.model 
    

class BikeInventory(models.Model):
    bikes_count = models.IntegerField() # Quantidade de motos no estoque
    bikes_value = models.FloatField() # Valor total das motos no estoque
    created_at = models.DateTimeField(auto_now_add=True) # Data de criação do registro
    updated_at = models.DateTimeField(auto_now=True) # Data de atualização do registro

    class Meta:
        ordering = ['-created_at'] # Ordena os registros pela data de criação, do mais recente para o mais antigo

    def __str__(self):
        return f'Bikes - {self.bikes_count} - {self.bikes_value}'