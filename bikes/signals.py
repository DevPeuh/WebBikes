# signals.py é um arquivo onde podemos definir funções que serão executadas quando determinados eventos ocorrerem em nossos modelos. Por exemplo, podemos definir uma função que será executada toda vez que um objeto do modelo Bike for salvo ou deletado. Isso é útil para realizar ações adicionais, como enviar notificações, atualizar outros modelos relacionados, ou simplesmente para fins de logging.

from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver # receiver é um decorador que serve para registrar a função como um receptor de sinais, ou seja, ela será chamada quando o sinal for emitido
from bikes.models import Bike, BikeInventory


def bike_inventory_update():
    bike_count = Bike.objects.all().count()
    bike_value = Bike.objects.aggregate(
        total_value = sum('value')
    )['total_value'] # a função aggregate é usada para realizar operações de agregação, como contar o número de objetos ou calcular a soma de um campo específico.
    BikeInventory.objects.create(
        bike_count = bike_count,
        bike_value = bike_value,
    )

@receiver(post_save, sender=Bike) 
def bike_post_save(sender, instance, **kwargs):# sender serve para identificar qual modelo está sendo salvo, instance é a instância do modelo que está sendo salva e **kwargs serve para receber outros argumentos que possam ser passados
    bike_inventory_update()

@receiver(post_delete, sender=Bike)
def bike_post_delete(sender, instance, **kwargs):
    bike_inventory_update()
    