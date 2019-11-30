from django.db import models

class Food(models.Model):
    name = models.CharField(verbose_name="Food Name", max_length=200)
    calories = models.FloatField(verbose_name="Calories (kcal)")
    total_fat = models.FloatField(verbose_name="Total Fat (g)")
    saturated_fat = models.FloatField(verbose_name="Saturated Fat (g)")

class Meal(models.Model):
    BREAKFAST = 1
    LUNCH = 2
    MEAL_TIME_TYPES = (
        (BREAKFAST, "Breakfast"),
        (LUNCH, "Lunch") 
     )	
    food = models.ForeignKey(Food, verbose_name="Food",on_delete = models.CASCADE)
    serving_size = models.IntegerField(verbose_name="Serving Size")
    meal_time = models.IntegerField(verbose_name="Meal Time", choices=MEAL_TIME_TYPES)
# Create your models here.

class Totalcal:
    def __add__(self, other):
        self.cal = 0
        self.other = 0
        return Totalcal(self.cal + self.other)

    

