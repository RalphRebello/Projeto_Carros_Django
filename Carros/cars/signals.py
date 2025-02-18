from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory
from gemini_AI_api.client import get_car_ai_bio


def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
                                        total_value=Sum('value')
                                      ) ['total_value']
    
    CarInventory.objects.create(cars_count=cars_count,
                                cars_value=cars_value)
    



# PRE FUNCTIONS #
# @receiver(pre_save, sender=Car)
# def car_pre_save(sender, instance, **kwargs):
#     print('### PRE SAVE ###')


# @receiver(pre_delete, sender=Car)
# def car_pre_delete(sender, instance, **kwargs):
#     print('### PRE DELETE ###')


# PRE FUNCTIONS #
@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        ai_bio = get_car_ai_bio(instance.brand, instance.model, instance.model_year)
        instance.bio = ai_bio


# POST FUNCTIONS #
@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()
    

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()
 