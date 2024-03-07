from django.db import models
from django.urls import reverse
from src.order.models import CleaningType

class Lead(models.Model):
  cleaning_type=models.ForeignKey(
    CleaningType,
    on_delete=models.PROTECT,
    verbose_name='Тип уборки'
  )
  counter_room=models.IntegerField(verbose_name='Количество комнат')
  counter_toilet=models.IntegerField(verbose_name='Количество санузлов')
  phone_number=models.IntegerField(verbose_name='Номер телефона')
  
  class Meta:
    verbose_name='Лид'
    verbose_name_plural='Лиды'
    
  def __str__(self):
    return self.phone_number
  
  def get_absolute_url(self):
      return reverse("lead_detail", kwargs={"pk": self.pk})
  
    
    