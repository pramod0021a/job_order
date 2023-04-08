from django.db import models

# Create your models here.
class Job(models.Model):
   customer_name = models.CharField(max_length=100)
   item_name = models.CharField(max_length=100)
   price = models.PositiveIntegerField()
   quantity = models.PositiveIntegerField()
   total_price = models.PositiveIntegerField(blank=True)   
   date = models.DateTimeField(auto_now_add=True)
   def save(self, *args, **kwargs):
      self.total_price = self.price * self.quantity
      super().save(*args, **kwargs)

   def __str__(self):
      return " {} - {} items for {}".format(self.customer_name, self.item_name,  self.total_price)

   


