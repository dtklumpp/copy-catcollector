from django.db import models
from django.contrib.auth.models import User

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

# Create your models here.

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    # more black magic from django
    toys = models.ManyToManyField(Toy) # creates a join table and then you will be able to acceess the join table 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# this is an example of a join table that django creates for us
# class Cat_Toys(models.Model):
#     cat_id = models.ForeignKey(Cat, on_delete=models.CASCADE)
#     toy_id = models.ForeignKey(Toy, on_delete=models.CASCADE)


class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']


# Ways to create/query/edit/delete data:
# 1. Through the app (forms, links, etc)
# 2. Through the Django/Python shell (python3 manage.py shell)
# 3. Through the psql shell
# 4. Through the admin panel at /admin